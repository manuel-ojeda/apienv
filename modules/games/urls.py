from django.conf.urls import url
from .views import ListGames, GameDetail

urlpatterns = [
	url(r'^$', ListGames.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', GameDetail.as_view()),
]