from django.contrib import admin
from .models import Faction

class FactionAdmin(admin.ModelAdmin):
	pass

admin.site.register(Faction, FactionAdmin)