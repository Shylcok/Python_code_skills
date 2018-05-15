# -*- coding: utf-8 -*-
# @Project : Python高效编程技巧实战
# @Time    : 0409
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : mysql_orm.py
# @Software: PyCharm
# ----------------------------------------------------
# import something
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

engine = create_engine("mysql://root:q107723403.@localhost/demo?charset=utf8")
Base = declarative_base()
Session = sessionmaker(bind=engine)


class News(Base):
    """
    orm
    """
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    images = Column(String(300), )
    author = Column(String(20), )
    view_count = Column(Integer)
    create_at = Column(DateTime)
    is_vaild = Column(Boolean)


class OrmTest:
    def __init__(self):
        self.session = Session()

    def add_one(self):
        # 新增记录
        new_obj = News(
            title='title',
            content='content',
            types='1'
        )
        new_obj2 = News(
            title='标题',
            content='内容',
            types='1'
        )
        self.session.add(new_obj)
        self.session.add(new_obj2)
        self.session.commit()
        return new_obj

    def get_one(self):
        # 查询记录
        return self.session.query(News).get(1)

    def get_more(self):
        # 查询多条记录
        return self.session.query(News).filter_by(is_vaild=True)

    def update_data(self, pk):
        # 修改数据
        obj = self.session.query(News).get(pk)
        if obj:
            obj.is_vaild = 0
            self.session.add(obj)
            self.session.commit()
            return True
        return False


def main():
    obj = OrmTest()
    # res = obj.add_one()
    # res = obj.get_more()
    # if res:
    #     for _ in res:
    #         print(_.id)
    # else:
    #     print('No exist!')
    res = obj.update_data(13)
    print(res)

if __name__ == '__main__':
    main()
