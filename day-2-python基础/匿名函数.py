# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0326
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 匿名函数.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
a = lambda x: x + 1


def cal(x):
    return x + 1


name = 'Felt'  # name = 'Felt_10'


def change_name(x):
    return x + '_10'


res = list(map(lambda x: name + '_10', [name, name, name]))
print(res)
name.startswith('F')