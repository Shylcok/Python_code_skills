# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0417
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : dict_for_each.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import random

d = {x: random.randint(60, 100) for x in 'abcdef'}

"""
for k in d equals for k in d.keys()
"""
for k in d:
    print(k, '->', d[k])

for k in d.keys():
    print(k, '->', d[k])
# values
for v in d.values():
    print('the value is {v}'.format(v=v))

# k&v
for k, v in d.items():
    print(k, '->', v)

# (k,v)
for (k, v) in d.items():
    print(k, '->', v)
