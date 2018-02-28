# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0223
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 算术运算.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


class New_int(int):
    def __radd__(self, other):
        return int.__sub__(self, other)


# a = New_int(3)
# b = New_int(5)
# print(a + b)
# print(divmod(a, b))

class Nint(int):
    def __rsub__(self, other):
        return int.__sub__(self, other)
a = Nint(5)
b = Nint(3)
print(3-a)
print(b+1)

