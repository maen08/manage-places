from rest_framework import serializers
from .models import Place


class PlaceSerializers(serializers.ModelSerializer):
    model = Place
    fields = '__all__'