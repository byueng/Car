#!
# -*-coding:utf-8 -*-
"""
@File Name: urls.py
@Author: jwm
@Date: 2025-02-10
@Description: writen by jwm

"""
from django.urls import path 
from .views import *

urlpatterns = [
    path("test/", test),
    path("login/", login), 
    path("register/", register),
]
