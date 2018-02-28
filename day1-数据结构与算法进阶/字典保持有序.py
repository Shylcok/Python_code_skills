# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0217
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 字典保持有序.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
d = {'jim': (1, 35), 'leo': (2, 37), 'bob': (3, 40)}
for k in d:
    pass
    # print(k,'\n')

from collections import OrderedDict

d1 = OrderedDict()

d1['jim'] = (1, 35)
d1['leo'] = (2, 37)
d1['bob'] = (3, 40)
# for k in d1:print(k)


######################################
from time import time
from collections import OrderedDict
from random import randint

d3 = OrderedDict()
players = list("abcdefgh")
start = time()

for i in range(8):
    input()
    # 阻塞函数
    p = players.pop(randint(0, 7-i))
    end = time()
    d3[p] = (i+1 , end - start)
    print(i + 1,
          p,
          end-start)
print('\n')
print('#'*20)

for k in d3:
    print(k,d3[k])