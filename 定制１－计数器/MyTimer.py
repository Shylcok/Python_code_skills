# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0223
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : MyTimer.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import time as t
import random as r


class MyTimer():
    def __init__(self):
        self.unit = ["年", '月', '日', '时', '分钟', '秒']
        self.prompt = '未开始计时'
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        """

        :param other:
        :return:
        """
        prompt = '总共运行了'
        result = []
        for i in range(6):
            result.append(self.lasted[i] + other.lasted[i])
            if result[i]:
                prompt += (str(result)[i] + self.unit[i])
        return prompt

    def start(self):
        """
        开始计时
        :return:
        """
        self.begin = t.localtime()
        self.prompt = '请先使用stop()停止计时！'
        print("计时开始．．．")

    def stop(self):
        """
        停止计时
        :return:
        """
        if not self.begin:
            print('提示：请调用start()进行计时！')
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束．．．")

    def _calc(self):
        """
        内部计算
        :return:
        """
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]


if __name__ == '__main__':
    t1 = MyTimer()
    print(t1)
    t1.start()
    t.sleep(r.randint(1, 3))
    t1.stop()
    print(t1)
