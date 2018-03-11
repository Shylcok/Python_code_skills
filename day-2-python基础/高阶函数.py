# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 高阶函数.py
# @Software: PyCharm
# ----------------------------------------------------
# 高阶函数定义:
# 1.函数接收的参数是一个函数名
# 2.函数的返回值是一个函数名
# 3.满足上述条件任意一个,都可称之为高阶函数
# ----------------------------------------------------
# import something
import time

#
# def foo():
#     print('我的函数名作为参数传给高阶函数')
#
#
# def goajie_1(func):
#     s = time.time()
#     time.sleep(0.2)
#     func()
#     e = time.time()
#     print('函数运行时间为{}'.format(e - s))
#
#
# def gaojie_2(func):
#     return func
#
#
# goajie_1(foo)
# foo = gaojie_2(foo)
# foo()

# 高阶函数总结
# 1.函数接收的参数是一个函数名
# 　　作用:在不修改函数源代码的前提下,为函数添加新功能,
# 　　不足:会改变函数的调用方式
# 2.函数的返回值是一个函数名
# 　　作用:不修改函数的调用方式
# 　　不足:不能添加新功能


def foo():
    time.sleep(1)
    print('I\'am foo')


"""
1.不修改被装饰函数的源代码（开放封闭原则）
2.为被装饰函数添加新功能后，不修改被修饰函数的调用方式
"""


# 多运行了一次
def timer(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print('函数%s的运行时间为%fs' % (func.__name__, (stop_time - start_time)))
    return func


foo = timer(foo)
foo()
