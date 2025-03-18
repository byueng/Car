#!
# -*-coding:utf-8 -*-
"""
@File Name: serializer.py
@Author: jwm
@Date: 2025-02-20
@Description: writen by jwm

"""
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['account', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone', 'email', 'birthdate']
        