# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0217
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 字典排序.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from random import randint

d = {x: randint(60, 100) for x in 'xyzabc'}
# print(d)
sorted(d)  # ['a', 'b', 'c', 'x', 'y', 'z']

print(sorted(zip(d.values(), d.keys())))
d.items()
sorted(d.items(), key=lambda x: x[1])
