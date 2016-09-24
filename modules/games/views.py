from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Game
from .serializers import GameSerializer
from django.http import Http404



class ListGames(APIView):
	def get(self, request):
		games = Game.objects.all()
		serializer = GameSerializer(games, many=True)
		return Response(serializer.data)



	def post(self, request):
		serializer = GameSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GameDetail(APIView):
	def get_object(self, pk):
		try:
			return Game.objects.get(pk=pk)
		except Game.DoesNotExist:
			raise Http404



	def get(self, request, pk, format=None):
		game = self.get_object(pk)
		serializer = GameSerializer(game)

		return Response(serializer.data)



	def put(self, request, pk, format=None):
		game = self.get_object(pk)
		serializer = FactionSerializer(Faction, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



	def delete(self, request, pk, format=None):
		game = self.get_object(pk)
		game.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)