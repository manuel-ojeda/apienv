from django.conf.urls import url
from .views import ListMaps, MapDetail

urlpatterns = [
	url(r'^$', ListMaps.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', MapDetail.as_view()),
]