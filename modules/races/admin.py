from django.contrib import admin
from .models import Race

class RaceAdmin(admin.ModelAdmin):
	pass

admin.site.register(Race, RaceAdmin)