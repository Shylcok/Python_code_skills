# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 生成器函数.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


def test():
    yield 1
    yield 2
    yield 3
    yield 4


if __name__ == '__main__':
    res = test()
    print(res.__next__())
    print(res.__next__())
    print(res.__next__())
    print(res.__next__())
