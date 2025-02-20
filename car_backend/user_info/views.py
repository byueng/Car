# built-in libaray
import time 

# django libaray
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# other python files
from .data_process import *
from .models import User


# test view 
def test(request):
    return HttpResponse(f"test successfully, current time: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}")

# user login view
@csrf_exempt
def login(request):
    '''
    login API

    Expected body format:
    {
        "account": "user_account",
        "password": "user_password"
    }
    '''

    if request.method == 'POST':
        body = load_body(request.body)
        account = body['account']
        password = body['password']
        try:
            user = User.objects.get(account=account)  # 查询数据库
            # 返回用户信息
            return JsonResponse({'account': user.account, 'password': user.password})
        
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=404)       
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)



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
        body = load_body(request.body)     
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
    