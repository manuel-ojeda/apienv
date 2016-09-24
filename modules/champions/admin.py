from django.contrib import admin
from .models import Champion

class ChampionAdmin(admin.ModelAdmin):
	pass

admin.site.register(Champion, ChampionAdmin)