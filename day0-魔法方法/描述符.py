# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0223
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 描述符.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 描述符　__get__ __set__ __delete__


class MyDescriptor:
    def __get__(self, instance, owner):
        print("getting...", self, instance, owner)

    def __set__(self, instance, value):
        print("setting...", self, instance, value)

    def __delete__(self, instance):
        print("deleting...", self, instance)


class Test:
    x = MyDescriptor()


class MyProperty:
    def __init(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)


class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    x = MyProperty(getX, setX, delX)


if __name__ == '__main__':
    test = Test()
    print(test.x)
    test.x = '1'
    print(test.x)
    del test.x
