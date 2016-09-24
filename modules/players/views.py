from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Player
from .serializers import PlayerSerializer
from django.http import Http404



class ListPlayers(APIView):
	def get(self, request):
		players = Player.objects.all()
		serializer = PlayerSerializer(players, many=True)
		return Response(serializer.data)



	def post(self, request):
		serializer = PlayerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PlayerDetail(APIView):
	def get_object(self, pk):
		try:
			return Player.objects.get(pk=pk)
		except Player.DoesNotExist:
			raise Http404



	def get(self, request, pk, format=None):
		player = self.get_object(pk)
		serializer = PlayerSerializer(player)

		return Response(serializer.data)



	def put(self, request, pk, format=None):
		player = self.get_object(pk)
		serializer = PlayerSerializer(Player, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



	def delete(self, request, pk, format=None):
		player = self.get_object(pk)
		player.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)