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
    # permission_classes = [IsAuthenticated]  

    # complete
    @csrf_exempt
    def get(self, request):
        '''
        Get Http request, return the user information to front

        ProfileSerializer format:
        {
            "phone": "user_phone"
            "email": "user_email"
            "birthdate": "user_birthdate"
        }

        :param request: Http request object
        :return Respone: Json type respone and the format is same as ProfileSerializer's with status 200 if successfully
        '''
        account = request.GET.get('account')
        try:
            if not account:
                return Response({"message": "用户不存在"}, status=404)
            else:
                user = User.objects.get(account=account)
                profile = Profile.objects.get(user=user)
                serializers = ProfileSerializer(profile)
                return Response(serializers.data, status=200)
        except: 
            return Response({'message': '出错了，请重试'}, status=404)     
                       
    @csrf_exempt
    def put(self, request):
        '''
        Put Http request, update the user information from front

        ProfileSerializer format:
        {
            "phone": "user_phone"
            "email": "user_email"
            "birthdate": "user_birthdate"
        }

        :param request: Http request object
        :return Respone: Json type respone with status 200 if successfully
        '''
        body = loads(request.body.decode('utf-8')) 
        user = User.objects.get(account=body['account'])
        profile = Profile.objects.get(user=user)
        profile.phone = body['phone']
        profile.email = body['email']
        profile.birthdate = body['birthdate']
        profile.save()
        serializers = ProfileSerializer(profile)
        return Response(serializers.data, status=200)

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
            profile = Profile(user=user)
            user.save()
            profile.save()
            return JsonResponse({'message': '用户创建成功，2秒后自动跳转到登录界面'}, status=201)
    else:
        return JsonResponse({'message': '错误的请求类型'}, status=405)
    
@csrf_exempt
def forget_password(request):
    """
    forget password api
    Expected body format:
    {
        account: "user who forget password",
        newPassword: "new password",
        confirmPassword: "confirm new password"
    }
    """
    if request.method == 'POST':
        body = loads(request.body.decode('utf-8'))
        account = body['account']
        newPassword = body['newPassword']
        try:
            user = User.objects.get(account=account)
            user.password = newPassword
            user.save()
            return JsonResponse({'message': '密码修改成功, 两秒后跳转到登陆界面'}, status=201)

        except User.DoesNotExist:
            return JsonResponse({'message': '用户不存在'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

