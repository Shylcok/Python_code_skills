# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0217
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 查找公共key.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from functools import reduce
from random import randint, sample

# sample('abcdefg',randint(3,6))
s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(
    s1,
    s2,
    s3
)

for k in s1:
    if k in s2 and k in s3:
        res = []
        res.append(k)

res1 = s1.keys()
res2 = s2.keys()
res3 = s3.keys()
print(res1 & res2 & res3)

########################################################

t = map(dict.keys, [s1, s2, s3])
print(t)

t2 = reduce(lambda a,b:a&b ,map(dict.keys, [s1, s2, s3]))
print(t2)