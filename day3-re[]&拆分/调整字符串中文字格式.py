# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 调整字符串中文字格式.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import re

log = open('/var/log/dpkg.log').read()
"""
re.sub: 捕获组
"""
t = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', log)
print(t)
