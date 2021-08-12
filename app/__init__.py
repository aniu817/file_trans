#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/5 08:22
# @Author : liu yang
# @Desc: 注册蓝图


from flask import Blueprint
from flask_restful import Api

from app.user.upload import Upload
from app.user.login import Login

user = Blueprint('user', __name__, url_prefix='/user')

user_api = Api(user)

user_api.add_resource(Upload, '/upload')
user_api.add_resource(Login, '/login')


