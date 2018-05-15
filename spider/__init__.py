# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0416
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : __init__.py.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = r'http://www.ziroom.com/z/nl/z3.html'
h2 = 'http://www.ziroom.com'
response = urlopen(html)

soup = BeautifulSoup(response, "lxml")
print(soup)
