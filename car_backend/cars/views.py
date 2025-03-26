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
            status=status.HTTP_200_OK
        )
    
    @csrf_exempt
    def post(self, request):
        """
        need body: {
            "brand": "car_brand",
            "model": "car_model",
            "price": "car_price",
            "age": "car_year",
            "image": "image_url"    
        }
        """
        serializer = CarInfo_Serializer(data=request.data)
        if serializer.is_valid():
            # 保存数据到数据库
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk=None):
        """
        删除指定的 CarInfo 实例
        """
        try:
            car = CarInfo.objects.get(pk=pk)  # 根据主键获取实例
            car.delete()  # 删除实例
            return Response({"message": "CarInfo deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except CarInfo.DoesNotExist:
            return Response({"error": "CarInfo not found"}, status=status.HTTP_404_NOT_FOUND)

class CarSearchView(APIView):
    @csrf_exempt
    def get(self, request):
        """
        get information: {
            "price": "price"
            "brand": "car_brand"
            "age": "car_age"
        }
        """
        brand = request.GET.get('brand')
        model = request.GET.get('model')
        price = request.GET.get('price')
        
        # 打印查询参数
        print(f"品牌: {brand}, 车型: {model}, 价格: {price}")

        # 构建查询条件
        filters = {}
        if brand:
            filters['brand__icontains'] = brand  # 模糊匹配品牌
        if price:
            filters['price'] = price  # 精确匹配价格
        if model:
            filters['model'] = model  # 精确匹配生产年份

        # 查询数据库
        cars = CarInfo.objects.filter(**filters)
        serializer = CarInfo_Serializer(cars, many=True)

        # 返回查询结果
        return Response(serializer.data, status=status.HTTP_200_OK)