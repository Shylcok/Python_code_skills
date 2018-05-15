# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0409
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : __init__.py.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import pymysql


class mysqlSreach:
    """mysql"""

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            self.coon = pymysql.Connect(
                host='127.0.0.1',
                user='root',
                password='q107723403.',
                db='article_spider',
                port=3306,
                charset='utf8'
            )
        except pymysql.Error as e:
            print('[-]Error %s ' % e)

    def close_coon(self):
        try:
            if self.coon:
                self.coon.close()
        except self.coon.Error as e:
            print('[-]Error %s ' % e)

    def get_one(self):
        sql = 'SELECT * FROM article_spider'

        cursor = self.coon.cursor()
        cursor.execute(sql)

        res = cursor.fetchall()

        for _ in res:
            yield _

        cursor.close()
        self.close_coon()
