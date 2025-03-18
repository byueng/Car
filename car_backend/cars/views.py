from json import loads

from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from .serializer import CarInfo_Serializer
from .models import CarInfo

# Create your views here.

class CarInfoView(APIView):
    @csrf_exempt
    def get(self, request):
        cars = CarInfo.objects.all().order_by('-id')[:8]
        serializer = CarInfo_Serializer(cars, many=True)
        return Response(
            serializer.data,
            status=201
        )
    
    @csrf_exempt
    def post(self, request):
        serializer = CarInfo_Serializer(data=request.data)
        if serializer.is_valid():
            # 保存数据到数据库
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # 返回错误信息
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
