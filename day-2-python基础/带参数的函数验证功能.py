# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0311
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 带参数的函数验证功能.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
user_list = [
    {'name': '123', 'passwd': '123'},
    {'name': '567', 'passwd': '123'},
    {'name': 'a', 'passwd': '123'},
    {'name': 'abc', 'passwd': '123'},
]

current_user = {'username': None, 'login': False}


def auth(auth_type='filedb'):
    def auth_func(func):
        def wrapper(*args, **kwargs):
            if current_user['username'] and current_user['login']:
                # 有用户登录
                res = func(*args, **kwargs)
                return res
            username = input('用户名: ').strip()
            passwd = input('密码: ').strip()
            for index, user_dic in enumerate(user_list):
                # 没有登录，新登录
                if username == user_dic['name'] and passwd == user_dic['passwd']:
                    current_user['username'] = username
                    current_user['login'] = True
                    res = func(*args, **kwargs)
                    return res
            else:
                # 用户名or密码错误
                print('用户名或者密码错误,重新登录')

        return wrapper


# auth(auth_type='file')就是在运行一个函数,然后返回auth_deco,所以@auth(auth_type='file')
# 就相当于@auth_deco,只不过现在,我们的auth_deco作为一个闭包的应用,外层的包auth给它留了一个auth_type='file'参数
@auth(auth_type='filedb')
def index():
    print('欢迎来到主页面')


@auth
def home():
    print('这里是你家')


@auth
def shopping_car():
    print('查看购物车啊亲')


@auth
def order():
    print('查看订单啊亲')


# print(user_list)
print('be4---->{}'.format(current_user))
index()
print('after---->{}'.format(current_user))
# print(user_list)
home()
