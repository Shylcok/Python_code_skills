# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0401
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 如何读写文件.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

"""
从python2---->python3
    str --> bytes
    unicode --> str
"""


"""
python2
>>> s = u'你好'
>>> s.encode('utf8')
'\xe4\xbd\xa0\xe5\xa5\xbd'
>>> s.encode('gbk')
'\xc4\xe3\xba\xc3'

解码必须统一：
>>> '\xe4\xbd\xa0\xe5\xa5\xbd'.decode('gbk')
u'\u6d63\u72b2\u30bd'

文件读写：
>>> f = open('python.txt','w')
>>> s = u'你好'
>>> f.write(s.encode('gbk'))
>>> f.close()
>>> f = open('python.txt','r')
>>> t = f.read()
>>> t
'\xc4\xe3\xba\xc3'
>>> t.decode('gbk')
u'\u4f60\u597d'
>>> print t.decode('gbk')
你好
"""



"""
python3
b'saasd'
'sadad' 默认为u'sadad'
"""
f = open('py3.txt', 'wt', encoding='utf8')
f.write('你好,')
f.close()
f = open('py3.txt','rt',encoding='utf8')
s = f.read()
print(s)