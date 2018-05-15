# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0401
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 如何设置文件缓冲.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
f = open('demo2.txt','w',buffering=0)
f.write('a')
