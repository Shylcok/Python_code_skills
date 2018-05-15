# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0415
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : sof_answer.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import random

diceboard = [1, 2, 0, 4, 5, 0]  # for example
n = 0


def roll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    dice5 = random.randint(1, 6)
    dice6 = random.randint(1, 6)
    return [dice1, dice2, dice3, dice4, dice5, dice6]


# while diceboard.index != 0:  # this basically means that per each element
# that does not have a value of zero(pls correct my code)
newroll = roll()

# newroll = newroll.split(None, n)[:n]  # this limits the size of the list
print(newroll)
for _ in range(0, len(diceboard) - 1):
    if diceboard[_] == 0:
        diceboard.pop(_)
for _ in range(0, len(newroll) - 1):
    if newroll[_] == 0:
        newroll.pop(_)
newroll = newroll.append(diceboard)
print(newroll)
