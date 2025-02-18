# built-in libaray
import time 

# django libaray
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# other python files
from .data_process import *


# test view 
def test(request):
    return HttpResponse(f"test successfully, current time: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}")

# user login view
@csrf_exempt
def login(request):
    if request.method == 'POST':
        body = load_body(request.body)
        
        return JsonResponse(
            body,
            status = 200
        )


@csrf_exempt
def register(request):
    if request.method == 'POST':
        body = load_body(request.body)      

        return JsonResponse(
            body
        )
    