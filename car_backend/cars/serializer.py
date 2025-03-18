from rest_framework import serializers
from .models import *

class CarInfo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CarInfo
        fields = ['brand', 'price', 'year', 'image']