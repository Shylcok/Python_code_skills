# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0226
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : nametuple_test.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from collections import *

# class User:
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height
#
#
# user = User(name='Felt', age=22, height=180)
# print(user.name, user.age, user.height)

User = namedtuple("User", ["name", "age", "height", "edu"])
user_tuple = ('Felt', 22, 180)
user = User(*user_tuple, "xsyu")


# print(user)


# 函数参数
def ask(*args, **kwargs):
    pass


ask(id='1', age=29)
