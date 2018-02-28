# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0217
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 用户历史记录功能.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from random import randint
from collections import deque
import pickle

N = randint(0, 100)
history = deque([], 5)


def guess(K):
    if N == K:
        return True
    if K < N:
        print("%s is less-then N" % K)
    else:
        print("%s is greater-then N" % K)
    return False


while True:
    line = input("pls input a number:")
    if line.isdigit():
        k = int(line)
        history.append(k)
        pickle.dump(history,
                    open('/home/jyfelt/Python高效编程技巧实战/day1-数据结构与算法进阶/tem/history'),
                    'w')
        pickle.load(open(history))
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print(list(history))


