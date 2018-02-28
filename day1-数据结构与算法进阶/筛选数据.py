# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0217
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 筛选数据.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from timeit import timeit
from random import randint

###删除负数

data = [randint(-10, 10) for i in range(10)]
# filter
re1 = filter(lambda x: x >= 0, data)

re2 = [x for x in data if x>=0]

# timeit(re1)
# timeit(re2)

d = {x: randint(60, 100) for x in range(1, 20)}

r= {k:v for k,v in d.iteritems() if v>90}

s = set(data)
l = {x for x in s if x%3 == 0}