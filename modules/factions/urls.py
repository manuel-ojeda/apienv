from django.conf.urls import url
from .views import ListFactions, FactionDetail

urlpatterns = [
	url(r'^$', ListFactions.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', FactionDetail.as_view()),
]