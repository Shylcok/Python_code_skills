# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0222
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 实现反向迭代.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# l = [1, 2, 3, 4, 5]
# # l.reverse()
# l1 = l[::-1]
# for x in reversed(l):
#     print(x)


class floatrange():
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


if __name__ == '__main__':
    for x in reversed(floatrange(1.0, 4.0, 0.5)):
        print(x)

