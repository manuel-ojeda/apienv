from django.db import models
from django.contrib.postgres.fields import ArrayField
from modules.factions.models import Faction
from modules.races.models import Race



class Champion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=(('ML', 'Male'), ('FM', 'Female')))
    faction = models.ForeignKey(
        Faction,
        on_delete=models.CASCADE,
        null = True,
        related_name='champions'
        )
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        null = True
        )
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name