# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0424
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : state_of_file.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import os
os.stat('demo.txt')
os.lstat('demo.txt')
os.fstat('demo.txt')