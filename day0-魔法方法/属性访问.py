# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0223
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 属性访问.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
class C:
    def __init__(self, size=10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize)


# c = C()
# print(c.x)


class a:
    def __getattribute__(self, item):
        print("__getattribute__")
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print("__getattr__")

    def __setattr__(self, key, value):
        print('__setattr__')
        return super().__setattr__(key, value)

    def __delattr__(self, item):
        print("__delattr__")
        super().__delattr__(item)


# z =a()
# z.x = 1
# print(z.x)


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == 'square':
            self.width = value
            self.height = value
        else:
            self.__dict__[key] = value
            super().__setattr__(key, value)

    def getArea(self):
        return self.width * self.height


if __name__ == '__main__':
    r1 = Rectangle(3, 4)
    print(r1.height)
    print(r1.getArea())
