# built-in libaray
import time 
from json import loads


# django libaray
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt



# test view 
def test(request):
    return HttpResponse(f"test successfully, current time: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}")

# user login view
@csrf_exempt
def login(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body:dict[str: str] = loads(body_unicode)
        username = body['username']
        
        return JsonResponse(
            {'username': username},
            status = 200
        )
