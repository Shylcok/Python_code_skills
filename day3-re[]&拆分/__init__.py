# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : __init__.py.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import re

line = 'j222222222222jyjfelt123'
# regex_str = '^j.*'
regex_str = '.*?(j.*?j).*'
res = re.match(regex_str, line)
if res:
    ret = res.group(1)
    print(ret)