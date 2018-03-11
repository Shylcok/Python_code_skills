# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 去掉字符串中不需要的字符.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 方法１
# [l/r]strip()
s = '   abc  123  '
s1 = '----abc++++'

res = s.strip()
res1 = s1.strip('+-')

print(res)
print(res1)
