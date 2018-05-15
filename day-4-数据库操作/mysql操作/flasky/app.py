# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0410
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : app.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
