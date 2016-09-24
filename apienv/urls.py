from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/champions/', include('modules.champions.urls', namespace="champions")),
    url(r'^api/factions/', include('modules.factions.urls', namespace="factions")),
    url(r'^api/games/', include('modules.games.urls', namespace="games")),
    url(r'^api/maps/', include('modules.maps.urls', namespace="maps")),
    url(r'^api/players/', include('modules.players.urls', namespace="players")),
    url(r'^api/races/', include('modules.races.urls', namespace="races")),
    url(r'^api/teams/', include('modules.teams.urls', namespace="teams")),

    # RUTA PARA AUTENTICACIÓN

    url(r'api-auth/', obtain_jwt_token)
]
