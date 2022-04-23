from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework import status
from .serializers import PlaceSerializers
from rest_framework.response import Response
from .models import Place
from django.shortcuts import get_object_or_404

class PlaceView(ViewSet):
	def create(self, request):
		serializer = PlaceSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors)
	  

	def list(self, request):
		queryset = Place.objects.all()
		serializer = PlaceSerializers(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


	def retrieve(self, request, slug=None):
		query = get_object_or_404(Place, slug=slug)
		serializer = PlaceSerializers(query)
		return Response(serializer.data, status=status.HTTP_200_OK)
	

	def destroy(self, request, slug=None):
		query = get_object_or_404(Place, slug=slug)
		serializer = PlaceSerializers(query)
		serializer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


	def partial_update(self, request, slug=None):
		details = get_object_or_404(Place, slug=slug)
		serializer = PlaceSerializers(
			instance=details, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors)




