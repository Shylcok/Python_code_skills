# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0426
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : callable.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import numpy as np
import matplotlib.pyplot as plt


def linear(a, b):
    def res(x):
        return a * x + b

    return res


cost = linear(0.3,5)
x = np.random.ranf(100)
y = cost(x)



plt.scatter(x,y)
plt.show()