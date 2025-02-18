#!
# -*-coding:utf-8 -*-
"""
@File Name: data_process.py
@Author: jwm
@Date: 2025-02-18
@Description: writen by jwm

"""

from json import loads

def load_body(body) -> dict[str: str]:
    return loads(body.decode('utf-8'))