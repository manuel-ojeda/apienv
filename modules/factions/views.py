from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Faction
from .serializers import FactionSerializer
from django.http import Http404



class ListFactions(APIView):
	def get(self, request):
		factions = Faction.objects.all()
		serializer = FactionSerializer(factions, many=True)
		return Response(serializer.data)



	def post(self, request):
		serializer = FactionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FactionDetail(APIView):
	def get_object(self, pk):
		try:
			return Faction.objects.get(pk=pk)
		except Faction.DoesNotExist:
			raise Http404



	def get(self, request, pk, format=None):
		faction = self.get_object(pk)
		serializer = FactionSerializer(faction)

		return Response(serializer.data)



	def put(self, request, pk, format=None):
		faction = self.get_object(pk)
		serializer = FactionSerializer(Faction, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		

	def delete(self, request, pk, format=None):
		faction = self.get_object(pk)
		faction.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)