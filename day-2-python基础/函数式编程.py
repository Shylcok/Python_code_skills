# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0408
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 函数式编程.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from functools import reduce

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x > 5, a)
print(list(b))
c = map(lambda x: x * 2, a)
print(list(c))
d = reduce(lambda x, y: x * y, range(1, 4))
print(d)
