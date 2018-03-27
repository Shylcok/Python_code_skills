# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0326
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 作用域.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
name = 'Felt'


def foo():
    name = 'foo'

    def bar():
        print(name)

    return bar


a = foo()
a()  # 输出最近的变量
# 1、作用域即范围
#       - 全局范围（内置名称空间与全局名称空间属于该范围）：全局存活，全局有效
#     - 局部范围（局部名称空间属于该范围）：临时存活，局部有效
# 2、作用域关系是在函数定义阶段就已经固定的，与函数的调用位置无关，如下
x = 1


def f1():
    def f2():
        print(x)

    return f2


x = 100


def f3(func):
    x = 2
    func()


x = 10000
f3(f1())

# 3、查看作用域：globals(),locals()


"""LEGB 代表名字查找顺序: locals -> enclosing function -> globals -> __builtins__
locals 是函数内的名字空间，包括局部变量和形参
enclosing 外部嵌套函数的名字空间（闭包中常见）
globals 全局变量，函数定义所在模块的名字空间
builtins 内置模块的名字空间"""
