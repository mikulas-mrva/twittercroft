import re
import json
import datetime

from .models import Country


def parse_interesting_fields(twitter_status):
    interesting_data = {
        'id': twitter_status.id,
        'text': twitter_status.text,
        'created_at': twitter_status.created_at,
        'display_profile_image': twitter_status.author.profile_image_url,
        'display_profile_url': twitter_status.author.url,
        'display_screen_name': twitter_status.author.screen_name,
        'display_full_name': twitter_status.author.name,
    }

    # override data tha differs for retweets
    if hasattr(twitter_status, 'retweeted_status'):
        original_status = twitter_status.retweeted_status
        interesting_data.update({
            'is_retweet': True,
            'display_screen_name': original_status.author.screen_name,
            'display_profile_image': original_status.author.profile_image_url,
            'display_profile_url': original_status.author.url,
            'display_full_name': original_status.author.name,
            'display_retweeter_name': twitter_status.author.name,
        })
    else:
        interesting_data.update({
            'is_retweet': False,
        })
    return interesting_data


def find_country_names(tweet):
    found_countries = set()

    # look for country names in hashtags
    hashtag_re = re.compile('#(\w+)')
    for result in hashtag_re.findall(tweet.get('text', '')):
        matching_countries = Country.objects.filter(camel_case_name__iexact=result)
        if matching_countries:
            found_countries.add(matching_countries.first())

    # look for capitalised country names in text
    capitalised_name_re = re.compile('(?P<phrase>(([A-Z][a-z]+)\s?)+)')
    for result in capitalised_name_re.findall(tweet.get('text', '')):
        for phrase in result:
            matching_countries = Country.objects.filter(name__iexact=phrase)
            if matching_countries:
                found_countries.add(matching_countries.first())

            # Indian->India etc
            if phrase[-2:] == 'an':
                matching_countries = Country.objects.filter(name__iexact=phrase[:-1])
                if matching_countries:
                    found_countries.add(matching_countries.first())

            # Chinese->China
            if phrase[-3:] == 'ese':
                matching_countries = Country.objects.filter(name__iexact=phrase[:-3]+'a')
                if matching_countries:
                    found_countries.add(matching_countries.first())

            # Javanese->Java
            if phrase[-4:] == 'nese':
                matching_countries = Country.objects.filter(name__iexact=phrase[:-4])
                if matching_countries:
                    found_countries.add(matching_countries.first())

            # ...perhaps add a few other trivial 'adjective detectors'

    tweet.update({'country_tags': found_countries})
    return tweet


def tweet_to_json(tweet):
    # country_tags is a set of objects that are not serializable
    if 'country_tags' in tweet:
        tweet['countries'] = [c.name for c in tweet.get('country_tags', set())]
        del(tweet['country_tags'])

    def date_handler(obj):
        if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
            return obj.isoformat()
        else:
            return None

    if 'created_at' in tweet:
        tweet['created_at'] = json.dumps(datetime.datetime.now(), default=date_handler)
    return tweet


def group_tweets_by_country(tweets):
    # group tweets by country name
    tweets_by_country = {}
    for tweet in tweets:
        try:
            if len(tweet.get('country_tags', [])):
                for country in tweet.get('country_tags', None):
                    if country.name in tweets_by_country:
                        tweets_by_country[country.name].append(tweet)
                    else:
                        tweets_by_country[country.name] = [tweet]
        except AttributeError:
            pass

    # transform to json
    tweet_list_by_country = []
    for country_name in tweets_by_country.keys():
        tweet_list_by_country.append(
            {
                'country': country_name,
                'number_of_mentions': len(tweets_by_country[country_name]),
                'tweets': [tweet_to_json(t) for t in tweets_by_country[country_name]]
             }
        )
    return json.dumps(tweet_list_by_country)
