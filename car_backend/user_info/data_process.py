#!
# -*-coding:utf-8 -*-
"""
@File Name: data_process.py
@Author: jwm
@Date: 2025-02-18
@Description: writen by jwm

"""

from json import loads


# load the request body
def load_body(body) -> dict[str: str]:
    data = loads(body.decode('utf-8'))
    return data

