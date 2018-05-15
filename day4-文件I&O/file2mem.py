# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0424
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : file2mem.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import mmap
f = open('demo.bin','r+b')
m = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)
