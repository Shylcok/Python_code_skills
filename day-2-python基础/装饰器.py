# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 装饰器.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import time


def timer(func):
    """
    装饰器=高阶函数+函数嵌套+闭包
    装饰器的框架
    :param func:
    :return:
    """

    def wrapper():
        s = time.time()
        func()
        e = time.time()
        print('the func %s runnig time is %f' % (func.__name__, e - s))

    return wrapper


def foo():
    time.sleep(0.2)
    print('this is func foo!')


if __name__ == '__main__':
    foo = timer(foo)
    foo()
