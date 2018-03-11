# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 装饰器加上返回值.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import time


def timer(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        res = func(*args, **kwargs)
        e = time.time()
        print('the func ["%s"]\'s runnig time is %f' % (func.__name__, e - s))
        return res

    return wrapper


# 语法糖
@timer  # run = timer(run)
def run(name, age):
    time.sleep(0.3)
    print('run!\nname:%s\nage:%d\n' % (name, age))
    return 'run的返回值'


# 语法糖
@timer  # run = timer(run)
def run1(name, age, gender):
    time.sleep(0.3)
    print('run!\nname:%s\nage:%d\ngender:%s\n' % (name, age, gender))
    return 'run的返回值'


if __name__ == '__main__':
    # run()
    run('a', 11)
    run1('a', 11, 'male')
