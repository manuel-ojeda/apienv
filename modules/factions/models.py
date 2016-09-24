from django.db import models
from django.contrib.postgres.fields import ArrayField



class Faction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
    	return self.name