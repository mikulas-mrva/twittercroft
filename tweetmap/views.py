from django.shortcuts import render
from django.views.generic.base import TemplateView

from .services import MaplecroftTwitter


class IndexPage(TemplateView):
    def get(self,request, *args, **kwargs):
        twitter_service = MaplecroftTwitter()
        tweet_list = twitter_service.get_n_latest_tweets()
        return render(request, 'tweetmap/index.html', {'tweets': tweet_list})
