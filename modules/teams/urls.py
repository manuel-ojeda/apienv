from django.conf.urls import url
from .views import ListTeams, TeamDetail

urlpatterns = [
	url(r'^$', ListTeams.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', TeamDetail.as_view()),
]