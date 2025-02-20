# built-in libaray
import time 
from json import loads

# django libaray
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# other python files
from .serializer import *
from .models import *

# complete
@csrf_exempt
def test(request):
    '''
    Use for testing
    '''
    return HttpResponse(f"test successfully, current time: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}")


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        profile = Profile.objects.get(user=request.user) 
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


# complete
@csrf_exempt
def login(request):
    '''
    login API

    Expected body format:
    {
        "account": "user_account",
        "password": "user_password"
    }

    :param request: Http request object
    :return: JsonRespone with status 200 if successful
    '''
    if request.method == 'POST':
        body = loads(request.body.decode('utf-8')) 
        account = body['account']
        password = body['password']
        try:
            user = User.objects.get(account=account)  # 查询数据库
            if password == user.password:
                return JsonResponse({'message': '登录成功，2秒后跳转到主页'}, status=201)
            else:
                return JsonResponse({'message': '密码错误，请重试'}, status=404)        
        except User.DoesNotExist:
            return JsonResponse({'message': '用户不存在'}, status=404)       
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

# complete
@csrf_exempt
def register(request):
    '''
    register API.

    Expected body format:
    {
        "account": "user_account",
        "password": "user_password",
    }

    :param request: Http request object
    :return: JsonRespone with status 200 if successful
    
    '''
    if request.method == 'POST':
        body = loads(request.body.decode('utf-8'))   
        account = body['account']
        password = body['password']
        flag = User.objects.filter(account=account).exists()        
        if flag:
            return JsonResponse({'message': '创建失败，新建用户名已存在，请重试'}, status=404)
        else:
            user = User(account=account, password=password)
            user.save()
            return JsonResponse({'message': '用户创建成功，2秒后自动跳转到登录界面'}, status=201)
    else:
        return JsonResponse({'message': '错误的请求类型'}, status=405)
    