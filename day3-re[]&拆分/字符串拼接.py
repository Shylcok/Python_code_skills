# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 字符串拼接.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

# s1 = 'abcdefg'
# s2 = '12345'
# res = s1 + s2
# str.__add__(s1, s2)
# s1>s2
# str.__gt__(s1,s2)
# print(res)

pl = ['<100>', '<21>', '<10x10>', '<60>', '<100.0>', '<500.0>']
s = ''
for p in pl:
    s += p

a = ''.join(pl)
print(a)