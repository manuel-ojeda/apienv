from django.db import models
from django.contrib.postgres.fields import ArrayField



class Map(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)