from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Champion
from .serializers import ChampionSerializer
from django.http import HttpResponse, Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .permissions import ApiUserPermissions



class ListChampions(APIView):
	permissions_classes = (ApiUserPermissions,)
	authentication_classes = (JSONWebTokenAuthentication,)
	
	def get(self, request):
		champions = Champion.objects.all()
		serializer = ChampionSerializer(champions, many=True)
		print (request.user.username)
		return Response(serializer.data)



	def post(self, request):
		serializer = ChampionSerializer(data=request.data)
		
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ChampionDetail(APIView):
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)

	def get_object(self, pk):
		try:
			return Champion.objects.get(pk=pk)
		except Champion.DoesNotExist:
			raise Http404



	def get(self, request, pk, format=None):
		champion = self.get_object(pk)
		serializer = ChampionSerializer(champion)

		return Response(serializer.data)



	def put(self, request, pk, format=None):
		champion = self.get_object(pk)
		serializer = ChampionSerializer(Faction, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		

	def delete(self, request, pk, format=None):
		champion = self.get_object(pk)
		champion.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)