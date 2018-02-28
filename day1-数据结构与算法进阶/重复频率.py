# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0217
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 重复频率.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from random import randint
from collections import Counter
data = [randint(0, 20) for i in range(30)]
# print(data)
c = dict.fromkeys(data, 0)
# print(c)

for x in data:
    c[x] += 1
# print(c)

# 排序
c2 = Counter(data)
print(c2.most_common(3))

# 词频统计
import re
txt = open('/home/jyfelt/Python高效编程技巧实战/jane').read()
c3 = Counter(re.split('\W+', txt))
print(c3.most_common(10))