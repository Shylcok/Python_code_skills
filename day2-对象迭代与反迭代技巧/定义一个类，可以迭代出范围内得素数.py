# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0220
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 定义一个类，可以迭代出范围内得素数.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

# def f():
#     print('in f() 1')
#     yield 1
#     print('in f() 2')
#     yield 2
#     print('in f() 3')
#     yield 3
#
#
# g = f()
#
# print(g.__iter__())
# print(g.__next__())
# t = g.__iter__() is g
# print(t)


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNUum(self, k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
            return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.isPrimeNUum(k):
                yield k


for x in PrimeNumbers(1, 100):
    print(x)
