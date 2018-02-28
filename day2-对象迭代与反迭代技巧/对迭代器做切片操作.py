# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0223
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 对迭代器做切片操作.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# f = open('/var/log/auth.log')
# lines = f.readlines()
# for line in lines:
#     print(line)
#
from itertools import islice
#
# for i in islice(f, 100, 110): print(i)

l = range(20)
t = iter(l)
for x in islice(t, 5, 10):
    print(x)

for x in t:
    print(x)