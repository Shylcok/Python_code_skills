# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0317
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 使用__new__方法.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


"""
在上面的代码中，
我们将类的实例和一个类变量 _instance 关联起来，
如果 cls._instance 为 None 则创建实例，
否则直接返回 cls._instance。
"""


class Myclass(Singleton):
    a = 1


if __name__ == '__main__':
    one = Myclass()
    tow = Myclass()
    print(one is tow)
    print(one == tow)
    print(id(one))
    print(id(tow))
