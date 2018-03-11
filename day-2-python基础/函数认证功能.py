# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 函数认证功能.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
USER_DICT = {
    'USER_NAME': None,
    'LOGIN_STAT': False
}


def auth_dunc(func):
    def wrapper(*args, **kwargs):
        if USER_DICT['USER_NAME'] and USER_DICT['LOGIN_STAT']:
            res = func(*args, **kwargs)
            return res
        else:
            username = input('Username:\n').strip()
            password = input('Password:\n').strip()
            # 如何记录登录状态？
            if username == '123' and password == '123':
                USER_DICT['USER_NAME'] = username
                USER_DICT['LOGIN_STAT'] = True
                print('login in!!!')
                res = func(*args, **kwargs)
                return res
            else:
                print('username or password wrong!')

    return wrapper


def index():
    print('this is index page')
    pass


@auth_dunc
def home(name):
    print('this is home page, {}'.format(name))
    pass


@auth_dunc
def shopping_car(name):
    print('this is shopping_car page, {}'.format(name))
    pass


@auth_dunc
def order():
    print('this is order page')
    pass


if __name__ == '__main__':
    home('Felt')
    shopping_car('Felt')
