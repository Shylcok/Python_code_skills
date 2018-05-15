# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : __init__.py.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import time



def get_bin_diff(m, n):
    a = str(bin(m))
    b = str(bin(n))
    count = 0
    if len(a) == len(b):

        for x in range(0, len(a) - 1):
            if a[x] is not b[x]:
                count += 1
        return count
    elif len(a) > len(b):
        zero_count = len(a) - len(b)

        list1 = []
        list2 = []
        [list1.append(x) for x in a.replace("0b", '')]
        [list2.append(x) for x in b.replace("0b", '')]

        new_1 = list1[::-1]
        new_2 = list2[::-1]

        [new_2.append('0') for _ in range(0, zero_count)]
        for x in range(0, len(new_2) - 1):
            if new_1[x] is not new_2[x]:
                count += 1
        return count + 1
    elif len(b) > len(a):
        zero_count = len(b) - len(a)

        list1 = []
        list2 = []
        [list1.append(x) for x in a.replace("0b", '')]
        [list2.append(x) for x in b.replace("0b", '')]

        new_1 = list1[::-1]
        [new_1.append('0') for _ in range(0, zero_count)]
        new_2 = list2[::-1]

        for x in range(0, len(new_2) - 1):
            if new_1[x] is not new_2[x]:
                count += 1
        return count + 1


def main():
    res = get_bin_diff(1, 2)
    print(res)


def timer(func):
    """
    装饰器=高阶函数+函数嵌套+闭包
    装饰器的框架
    :param func:
    :return:
    """

    def wrapper():
        s = time.time()
        func()
        e = time.time()
        print('the func %s runnig time is %s' % (func.__name__, e - s))

    return wrapper

@timer
def bin_k():
    v = input()
    a, b, c = v.split(' ')
    res = 2 ** int(a) + 2 ** int(b) - 2 ** int(c)
    ret = bin(res)
    count = 0
    print(ret)
    for x in str(ret):
        if x == "1":
            count += 1
    print(count)


if __name__ == '__main__':
    bin_k()
    pass
