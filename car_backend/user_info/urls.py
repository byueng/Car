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
    path("profile/", ProfileView.as_view(), name='profile'),
    path("forgetpassword/", forget_password),
    path("remove_favorite/", RemoveFavoriteView.as_view())
]
