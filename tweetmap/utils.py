import re

from .models import Country

def parse_interesting_fields(twitter_status):
    # todo include retweets?
    interesting_data = {
        'text': twitter_status.text,
        'created_at': twitter_status.created_at,
        'display_profile_image': twitter_status.author.profile_image_url,
        'display_profile_url': twitter_status.author.url,
        'display_screen_name': twitter_status.author.screen_name,
        'display_full_name': twitter_status.author.name,
    }
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

    # country names in hashtags
    hashtag_re = re.compile('#(\w+)')
    for result in hashtag_re.findall(tweet.get('text', '')):
        matching_countries = Country.objects.filter(camel_case_name__iexact=result)
        if matching_countries:
            found_countries.add(matching_countries.first())

    # capitalised country names in text
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

    tweet.update({'country_tags': found_countries})

    return tweet
