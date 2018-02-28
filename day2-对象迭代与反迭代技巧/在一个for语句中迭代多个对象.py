# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0223
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 在一个for语句中迭代多个对象.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 1.并行
from random import randint

math = [randint(60, 100) for _ in range(40)]
english = [randint(60, 100) for _ in range(40)]
chinese = [randint(60, 100) for _ in range(40)]

# for i in range(len(math)):
#     t = math[i] + english[i] + chinese[i]

total = []
for c, m, e in zip(chinese, math, english):
    total.append(c + m + e)

print(total)
# 2.串行
from itertools import chain

e1 = [randint(60, 100) for _ in range(40)]
e2 = [randint(60, 100) for _ in range(42)]
e3 = [randint(60, 100) for _ in range(41)]
e4 = [randint(60, 100) for _ in range(39)]
count = 0
for s in chain(e1, e2, e3, e4):
    if s > 90:
        count += 1
print(count)
