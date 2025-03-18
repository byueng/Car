from django.urls import path 
from .views import *

urlpatterns = [
    path('info/', CarInfoView.as_view()),
]