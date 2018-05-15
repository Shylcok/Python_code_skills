# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0414
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 随机数据生成.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import random


def random_list(n):
    a = []

    ids = list(range(1000, 1000 + n))
    f_name = ['赵', '孙', '王', '李', '周']
    s_name = ['爱', '立', '军', '予', '莫', '白']
    l_name = ['华', '天', '安', '宝', '坤', '铭']
    for i in range(n):
        b = {}
        age = random.randint(18, 60)
        id_ = ids[i]
        name = random.choice(f_name) + random.choice(s_name) + random.choice(l_name)

        b['id'] = id_
        b['age'] = age
        b['name'] = name
        a.append(b)
    # dict.fromkeys(seq[, val])
    # 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
    return a


res = random_list(10)
for di in res:
    print(di)
