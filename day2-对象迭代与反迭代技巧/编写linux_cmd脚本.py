# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0221
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 编写linux_cmd脚本.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import subprocess


def conn(**kwargs):
    param = kwargs['user'] + '@' + kwargs['address']
    print(param)
    p = subprocess.Popen(['ssh', param], shell=True)
    while True:
        a = p.wait()
        print(a)
        if a == 0:
            print('ok')
            conn()
        else:
            p.kill()
            print('0')
            return


if __name__ == "__main__":
    param = ['root', '120.78.191.97']
    conn(user=param[0], address=param[1])
