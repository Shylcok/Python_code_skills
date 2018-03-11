# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 判断开头结尾.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import os, stat

res = [name for name in os.listdir('.') if name.endswith(('sh', 'c'))]
print(res)
stat1 = os.stat('a.c')
print(oct(stat1.st_mode))
os.chmod('a.c',stat1.st_mode|stat.S_IXUSR)