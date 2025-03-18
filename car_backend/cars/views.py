from json import loads

from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializer import CarInfo_Serializer
from .models import CarInfo

# Create your views here.

class CarInfoView(APIView):
    @csrf_exempt
    def get(self, request):
        cars = CarInfo.objects.all()[:8]
        serializer = CarInfo_Serializer(cars, many=True)
        return Response(
            serializer.data,
            status=201
        )

