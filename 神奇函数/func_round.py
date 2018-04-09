# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0401
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : func_round.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# import sys
#
# a = 1
# b = 2
# c = [a, b, [b, a]]
# res = sys.getrefcount(a)
# res1 = sys.getrefcount(b)
# res2 = sys.getrefcount(c)
# print(res)
# print(res1)
# print(res2)
# a = b
# res = sys.getrefcount(a)
# res1 = sys.getrefcount(b)
# res2 = sys.getrefcount(c)
# print(res)
# print(res1)
# print(res2)

import re

# p = re.compile('blue|red|white')
# print(p.sub('color', 'blue socks and red socks'))
# print(p.sub('color', 'blue socks and red socks', count=1))
# print(p.subn('color', 'blue socks and red socks'))
# print(p.subn('color', 'blue socks and red socks', count=1))
pattern = 'jyf'
string = 'jyfelt'
string1 = 'wadjajyfelt'
# print(re.match(pattern, string))
# print(re.search(pattern, string1))
# print(re.match(pattern, string).group())
# print(re.search(pattern, string1).group())
a = re.compile('(<.*?>)')
