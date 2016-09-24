from django.conf.urls import url
from .views import ListRaces, RaceDetail

urlpatterns = [
	url(r'^$', ListRaces.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', RaceDetail.as_view()),
]