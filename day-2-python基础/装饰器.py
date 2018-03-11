# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 装饰器.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 装饰器=高阶函数+函数嵌套+闭包
import time


def timer(func):
    def wapper(*args, **kwargs):
        start_time = time.time()
        res = wapper(*args, **kwargs)
        stop_time = time.time()
        print('函数%s的运行时间为%d' % (func, (start_time - stop_time)))
        return res
    return wapper()


@timer
def cal(l):
    # start_time = time.time()
    res = 0
    # time.sleep(0.2)
    for i in l:
        res += i

    # stop_time = time.time()
    print(res)  # 'time:{}'.format(start_time - stop_time))
    return res


cal(range(100))
