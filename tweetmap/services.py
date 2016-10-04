from django.conf import settings

from .utils import parse_interesting_fields

from tweepy import OAuthHandler, API


class MaplecroftTwitter(object):
    def __init__(self):
        auth = OAuthHandler(settings.TWITTER_API_CONSUMER_KEY, settings.TWITTER_API_CONSUMER_SECRET)
        auth.set_access_token(settings.TWITTER_API_ACCESS_TOKEN, settings.TWITTER_API_ACCESS_SECRET)

        self.api = API(auth)

        self.twitter_screen_name = settings.TWITTER_MAPLECROFT_SCRREEN_NAME
        self.default_number_of_tweets = settings.DEFAULT_NUMBER_OF_TWEETS

    def get_n_latest_tweets(self, number_of_tweets=None):
        if not number_of_tweets:
            number_of_tweets = settings.DEFAULT_NUMBER_OF_TWEETS

        # todo cache?
        tweets = map(
            parse_interesting_fields,
            self.api.user_timeline(screen_name=self.twitter_screen_name, count=number_of_tweets)
        )
        return tweets

