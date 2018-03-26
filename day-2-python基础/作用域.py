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
    bar()

foo()