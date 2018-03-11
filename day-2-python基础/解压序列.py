# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 解压序列.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from random import randint

# l = [randint(10, 20) for x in range(10)]
l = [10, 11, 18, 19, 16, 19, 18, 13, 19, 11]
a, *_, c = l
print(a)
print(_)
print(c)
