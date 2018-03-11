# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 字符串左右居中对齐.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# str.ljust()
# str.rjust()
# str.center()
s = 'abc'
res = s.rjust(20, '=')
res1 = s.ljust(20, '+')
res2 = s.center(20, '*')
print(res)
print(res1)
print(res2)

a = format(s, '<20')
b = format(s, '>20')
c = format(s, '^20')
print(a)
print(b)
print(c)

d = {'Name': 'Runoob',
     'Age': 7,
     'Class': 'First'}
list1 = list(map(len, d.keys()))
w = max(list1)
for k in d:
    print(k.ljust(w), ':', d[k])
