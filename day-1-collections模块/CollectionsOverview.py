# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0226
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : CollectionsOverview.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

from collections import *
# 　抽象基类 interface[java/kotlin]
from collections.abc import *

# __use__ = ['deque', 'defaultdict', 'namedtuple', 'Counter', 'OrderedDict', 'ChainMap']

# 不可变
name_tuple = ('1', '2')
# name_tuple = ('2', '2')
# for name in nametuple:
#     print(name)

"拆包"
user_tuple = ('shylock', 22, 180, 'it')
# name, age, height = user_tuple
name, *other = user_tuple
# name = user_tuple[0]
# age = user_tuple[1]
# height = user_tuple[2]
# print(name, age, height)
# print(name, other)

name_tuple = ('1', '2', [2, 9])
name_tuple[2].append(22)
# print(name_tuple)

# tuple -- immutable
# 1、性能优化　加速，常量
# 2、线程安全
# 3、可以作为dict的key (可以hash)
# 4、拆包特性

user_info_dict = {user_tuple: 'shylock'}
print(user_info_dict)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User(name='Felt', age=22)
print(user.name)