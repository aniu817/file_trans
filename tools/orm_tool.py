#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/11 16:06
# @Author : liu yang
# @Desc:ORM 操作


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User

from settings import Conf


class OrmTool:
    _scheme = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4'.format(Conf.NAME.value,
                                                                   Conf.PASSWORD.value,
                                                                   Conf.HOST.value,
                                                                   Conf.INSTANCE.value)

    _engine = create_engine(_scheme, pool_size=5, max_overflow=-1, pool_recycle=1200)

    _session = sessionmaker(_engine)
    _my_session = _session()

    @staticmethod
    def query_by_account(table_model, account):
        record = OrmTool._my_session.query(table_model).filter_by(account=account).first()
        if record is not None:
            try:
                return record.password
            finally:
                OrmTool._my_session.close()


if __name__ == "__main__":
    OrmTool.query_by_account(User, '123455')
