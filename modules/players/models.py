from django.db import models
from django.contrib.postgres.fields import ArrayField



class Player(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	birthday = models.DateField()
	gender = models.CharField(max_length=10, choices=(('ML', 'Male'), ('FM', 'Female')))