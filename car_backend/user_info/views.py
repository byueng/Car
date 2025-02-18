# built-in libaray
import time 
from json import loads

# django libaray
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


class search_sql_table:
    '''
    Usage for all mysql calculate with django
    '''
    def __init__(self):
        pass



# test view 
def test(request):
    return HttpResponse(f"test successfully, current time: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}")

# user login view
@csrf_exempt
def login(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body:dict[str: str] = loads(body_unicode)
        
        return JsonResponse(

        )
