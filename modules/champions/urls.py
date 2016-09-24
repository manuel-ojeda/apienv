from django.conf.urls import url
from .views import ListChampions, ChampionDetail

urlpatterns = [
	url(r'^$', ListChampions.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', ChampionDetail.as_view()),
]