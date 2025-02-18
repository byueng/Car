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
        
        return JsonResponse(
            body,
            status = 200
        )


@csrf_exempt
def register(request):
    '''
    register API.

    Expected body format:
    {
        "account": "user_account",
        "password": "user_password",
        "confirm_password": "user_confirm_password"
    }

    :param request: Http request object
    :return: JsonRespone with status 200 if successful
    
    '''
    if request.method == 'POST':
        body = load_body(request.body)     
        account = body['account']
        password = body['password']

        user = User(account=account, password=password)
        user.save()
        return JsonResponse({'message': '用户创建成功'}, status=201)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    