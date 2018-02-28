# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0223
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 继承.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
class Parent():
    def hello(self):
        print("正在调用基类的方法")


class Child(Parent):
    def hello(self):
        print("正在调用子类的方法")


import random as r


class Fish():
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print('我的位置是: ', self.x, self.y)


class G(Fish):
    pass


class C(Fish):
    pass


class S(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('我要吃')
            self.hungry = False
        if self.hungry == False:
            print('初步下了')


class C:
    def __init__(self, size=10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize )


class Parrot(object):
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage
