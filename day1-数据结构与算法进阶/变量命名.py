# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0217
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 变量命名.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

from collections import namedtuple

NAME, AGE, SEX, EMAIL = range(4)

student = ('jim', 16, 'male', '11@11.com')
# print(student[NAME])
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])

s = Student('jim', 16, 'male', '11@11.com')
# print(s.name)

print(isinstance(s, tuple))
