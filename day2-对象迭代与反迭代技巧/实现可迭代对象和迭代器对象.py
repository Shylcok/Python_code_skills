# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0220
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 实现可迭代对象和迭代器对象.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
l = [1, 2, 3, 4]
s = 'abcde'

print(iter(l))
print(l.__iter__)
print(iter(s))
print(s.__getitem__)

# for x in l:print(x)

t = iter(l)
print(t)
print(t.__next__())