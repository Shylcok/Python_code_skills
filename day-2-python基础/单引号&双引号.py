# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0407
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 单引号&双引号.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
s = 'Let\'s go'
s1 = "Let's go"
s2 = 'i really like "Python"'
s3 = """Let's go # hello"""


class a:
    def __str__(self):
        return 'This is class {__class__.__name__}'.format(__class__=__class__)

    def __repr__(self):
        return 'This is class {__class__.__name__}'.format(__class__=__class__)

    pass


A = a()
print(a)
print(A)


