# built-in libaray
import time 

# django libaray
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# test view 
def test(request):
    return HttpResponse(f"test successfully, current time: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}")

# user login view
def login(request):
    user_data = request.data
    return JsonResponse(user_data)
