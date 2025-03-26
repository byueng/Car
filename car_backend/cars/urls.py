from django.urls import path 
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('info/', CarInfoView.as_view()),
    path('info/<int:pk>/', CarInfoView.as_view(), name='car-info-detail'),
    path('search/', CarSearchView.as_view()),
]