# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0414
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 链表.py
# @Software: PyCharm
# ----------------------------------------------------
# import something


class LLode:
    def __init__(self, node, next_=None):
        self.node = node
        self.next_ = next_


class NodeList(object):

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def pre_add(self, elem):
        self._head = LLode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise EOFError
        e = self._head.node
        self._head = self._head.next_
        return e


my_list = NodeList()
print(my_list.is_empty())
my_list.pre_add('a')
print(my_list.is_empty())
my_list.pop()
print(my_list.is_empty())
my_list.pop()