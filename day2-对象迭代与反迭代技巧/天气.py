# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0220
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 天气.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import requests
from collections import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getweather(city)

    def getweather(self, city):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s : %s ,%s , %s' % (city, data['type'], data['high'], data['low'])


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


if __name__ == '__main__':
    for x in WeatherIterable('西安'):
        print(x)
