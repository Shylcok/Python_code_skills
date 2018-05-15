# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0424
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : csv_io.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import csv

# rf =open('000001.csv', 'rb')
# reader = csv.reader(rf)
# for x in reader:
#     print(x)
# wf = open('copy.csv','wb')
# writer = csv.writer(wf)
# writer.writerow(['a','b'])
with open('000001.csv', 'rb') as rf:
    reader = csv.reader(rf)
    with open('000002.csv', 'wb') as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headers)
        for row in reader:
            if int(row[6]) >= 50000000000:
                writer.writerow(row)
print('end')