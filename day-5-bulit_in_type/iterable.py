# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0417
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : iterable.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
def countdown(n):
    print('Counting down')
    while n > 0:
       yield n
       n -= 1

