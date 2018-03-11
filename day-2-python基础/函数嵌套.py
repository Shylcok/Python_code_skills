# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 函数嵌套.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


def father(name):
    # print('from father %s' % name)

    def son():
        print('my father is %s' % name)

    son()


if __name__ == '__main__':
    father('Felt')
