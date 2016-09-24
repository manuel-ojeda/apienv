from rest_framework import serializers
from .models import Faction
from modules.champions.serializers import ChampionSerializer

class FactionSerializer(serializers.ModelSerializer):
	factions = ChampionSerializer(many=True, read_only=True)

	class Meta:
		model = Faction