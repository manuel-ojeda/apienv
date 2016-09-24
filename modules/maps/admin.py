from django.contrib import admin
from .models import Map

class MapAdmin(admin.ModelAdmin):
	pass

admin.site.register(Map, MapAdmin)