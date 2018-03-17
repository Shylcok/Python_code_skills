# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0317
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : class_with_al.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
class myclass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plus(self):
        return self.a + self.b

    @staticmethod
    def staticmethdo_func():
        return "This is a static_func"

if __name__ == '__main__':
    newclass = myclass(1,2)
    print(newclass.plus())
    print(newclass.staticmethdo_func())