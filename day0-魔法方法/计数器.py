# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0223
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 计数器.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from time import localtime


class A():
    def __str__(self):
        return '你好'


a = A()
print(a)

class B():
    def __repr__(self):
        return "你好"

b = B()
print(b)
print()