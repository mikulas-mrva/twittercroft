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

    return tweet
