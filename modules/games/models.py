from django.db import models
from django.contrib.postgres.fields import ArrayField
from modules.maps.models import Map
from modules.teams.models import Team

class GameType(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateField()

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey(
        Map,
        on_delete=models.CASCADE,
        null=True
        )
    game_type = models.ForeignKey(
        GameType,
        on_delete=models.CASCADE,
        null=True
        )
    is_active = models.BooleanField(default=False)
    winner_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField()
    finished_at = models.DateField()