from django.shortcuts import render
from django.views.generic.base import TemplateView
from tweepy import TweepError

from .services import MaplecroftTwitter
from .utils import group_tweets_by_country


class IndexPage(TemplateView):
    def get(self,request, *args, **kwargs):
        twitter_service = MaplecroftTwitter()
        try:
            tweet_list = list(twitter_service.get_n_latest_tweets())
        except TweepError as e:
            tweet_data = {'tweepy_error': True}
        else:
            tweet_data = {
               'tweets': tweet_list,
                'tweets_json': group_tweets_by_country(tweet_list),
            }

        return render(request, 'tweetmap/index.html', tweet_data)
