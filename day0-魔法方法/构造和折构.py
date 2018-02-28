# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0223
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 构造和折构.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPeri(self):
        return (self.x + self.y) * 2

    def getArea(self):
        return self.x * self.y


rect = Rectangle(3, 4)
# print(rect.getArea())
# print(rect.getPeri())


# __new__(cls, *args, **kwargs) 第一个传入的参数
class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


# a = CapStr('UGHDWbjKBJBdBBJBJBJBbjbjbwjkabdkja')
# print(a)


# __del__(self) 垃圾处理机制
class C:
    def __init__(self):
        print("我是__init__方法，我被调用了")

    def __del__(self):
        print("我是__del__方法，我被调用了")


c1 = C()
