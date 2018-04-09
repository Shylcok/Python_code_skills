# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0408
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : duck_type.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
a = []
b = ()
c ={}
a.append(b)
a.append(c)
print(a)

b =list.extend(a,b)