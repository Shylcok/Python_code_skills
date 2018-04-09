# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0408
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 闭包.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
def outter(a):
    """
    闭包：
    在一个外函数中定义了一个内函数，
    内函数里运用了外函数的临时变量，
    并且外函数的返回值是内函数的引用。
    这样就构成了一个闭包。
    :param a:
    :return:
    """
    b = 10

    def inner():
        print(a + b)

    return inner

"""一般情况下，
在我们认知当中，如果一个函数结束，
函数的内部所有东西都会释放掉，
还给内存，局部变量都会消失。
但是闭包是一种特殊情况，
如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，
就把这个临时变量绑定给了内部函数，
然后自己再结束"""




if __name__ == '__main__':
    res = outter(5)
    res()
