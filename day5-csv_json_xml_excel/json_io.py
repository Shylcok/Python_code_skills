# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0424
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : json_io.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from aip import AipSpeech
from .config import *
""" 你的 APPID AK SK """
APP_ID = APP_ID
API_KEY = API_KEY
SECRET_KEY = SECRET_KEY

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

