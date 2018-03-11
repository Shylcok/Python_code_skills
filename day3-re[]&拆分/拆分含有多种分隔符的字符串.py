# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 拆分含有多种分隔符的字符串.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
"""
x = !ps aux
s = x[-1]
s
s.split()
"""


# res = s.split(';')
# t = []
# list1 = map(lambda x: t.extend(x.split('|')), res)
# print(list(list1))
# res = t
# t = []
# map(lambda x: t.extend(x.split('/')), res)

def mySpilt(s, ds):
    """
    run in python2
    :param s:
    :param ds:
    :return:
    """
    res = [s]
    for d in ds:
        t = []
        list(map(lambda x: t.extend(x.split(d)), res))
        res = t
    return [x for x in res if x]
    pass


if __name__ == '__main__':
    s = 'dad;wdad|wds/dwd,dwds\d\twd'
    print(mySpilt(s, ';|/\,\t'))

    import re
    a = re.split('[;,|/\t]+', s)
    print(a)