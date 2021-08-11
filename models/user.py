#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/10 16:47
# @Author : liu yang
# @Desc: User 对象


from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    # 表的名字:
    __tablename__ = 'login'

    # 表的结构:
    id = Column(String(32), primary_key=True)
    name = Column(String(20))
    account = Column(String(20))
    password = Column(String(64))
    create_time = Column(String(20))


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:rqg$^1ySohpq@10.100.0.210:3306/analysis?charset=utf8mb4')
    # Base.metadata.create_all(engine)
