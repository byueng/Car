#!
# -*-coding:utf-8 -*-
"""
@File Name: data_process.py
@Author: jwm
@Date: 2025-02-18
@Description: writen by jwm

"""

from json import loads
from .models import User


def load_body(body) -> dict[str: str]:
    '''
    Load the request body
    '''
    data = loads(body.decode('utf-8'))
    return data

def table_element_check(account: str):
    '''
    Check whether the element in the table of backend database.

    Excepted account format: "account"
    
    :param account: The account to check in the database
    :return: True if the account exists, False otherwise
    '''
    return User.objects.filter(account=account).exists()
    