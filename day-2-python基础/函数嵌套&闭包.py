# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 函数嵌套&闭包.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 嵌套＆作用域


def father(name):
    print('from father %s' % name)

    def son():
        # name = 'JY'
        print('my father is %s' % name)

        def grandson():
            name = 'idk'
            print('my grandfather is %s' % name)

        grandson()

    son()


if __name__ == '__main__':
    father('Felt')
