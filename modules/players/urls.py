from django.conf.urls import url
from .views import ListPlayers, PlayerDetail

urlpatterns = [
	url(r'^$', ListPlayers.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', PlayerDetail.as_view()),
]