# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 去掉字符串中不需要的字符.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

# 方法１
# [l/r]strip()
# s = '   abc  123  '
# s1 = '----abc++++'
#
# res = s.strip()
# res1 = s1.strip('+-')
#
# print(res)
# print(res1)

# 方法二
# res2 = 'abc:123'
# print(res2[:3] + res2[4:])
#
# s2 = '\tafv\twada\tada'
# a = s2.replace('\t', '')
# print(a)

# 方法3
# s = '\tafv\twada\tada\r'
# import re
#
# a = re.sub('[\r\t]', '', s)
# print(a)


# 方法四 python2
# import
# s = 'abc123321xyz'
# string.maketrans()
# s.translate()
s = '\tafv\twada\tada\r'
a = s.translate([0, '\t\r'])
print(a)