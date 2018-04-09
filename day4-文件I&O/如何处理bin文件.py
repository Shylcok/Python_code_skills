# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0401
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 如何处理bin文件.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import struct
# struct　处理二进制文
import array

f = open('卡农.wav', 'rb')

info = f.read(44)
# short:h int:i
a = struct.unpack('h', info[22:24])
b = struct.unpack('i', info[24:28])
c = struct.unpack('h', info[34:36])
print(a, b, c)

# 计算文件长度：
# 修改文件指针位置(seek)到文件最后:
f.seek(0, 2)
print(f.tell())
n = (f.tell() - 44) // 2
buf = array.array('h', (0 for _ in range(n)))
f.seek(44)
for i in range(n): buf[i] //= 8
for i in range(n): print(buf[i])

f.close()
