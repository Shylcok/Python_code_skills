# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0415
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : __init__.py.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


def foo():
    """
    this is func foo
    :return: a
    """
    a = 1

    return a


class a:
    def __init__(self):
        self.a = 1

    def __repr__(self):
        return 'this is %s' % __name__


# c = foo.__name__
# b = foo.__dict__
# d = foo.__code__
# print(type(d))
# print(c)
# print(b)
# print(foo.__doc__)
#
# print(a.__doc__)

def callfunc(func):
    return func()


def bar():
    print('this is func bar')

callfunc(bar)