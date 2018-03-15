# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0314
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : hello.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
import eel

eel.init('web')  # Give folder containing web files


@eel.expose  # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)


say_hello_py('Python World!')
eel.say_hello_js('Python World!')  # Call a Javascript function

eel.start('hello.html', size=(300, 200))  # Start