from django.shortcuts import render
from django.views.generic.base import TemplateView

from .services import MaplecroftTwitter
from .utils import group_tweets_by_country


class IndexPage(TemplateView):
    def get(self,request, *args, **kwargs):
        twitter_service = MaplecroftTwitter()
        tweet_list = list(twitter_service.get_n_latest_tweets())
        return render(request, 'tweetmap/index.html', {
            'tweets': tweet_list,
            'tweets_json': group_tweets_by_country(tweet_list),
        })
