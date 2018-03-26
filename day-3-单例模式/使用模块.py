# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0317
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 使用模块.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
# 其实，python的模块就是天然的单例模式,因为模块第一次导入时,会生成.pyc文件
# 当第二次导入时，就是直接加载.pyc文件，


from .mysingleton import my_singleton
my_singleton.foo()

