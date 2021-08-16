#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/16 08:23
# @Author : liu yang
# @Desc: user api


from flask import Blueprint
from flask_restx import Api
from app.user.upload import ns_upload
from app.user.login import ns_login
from app.user.final_upload import ns_final_upload


api_user = Blueprint('api_user', __name__, url_prefix='/user')

api = Api(
    api_user,
    version='1.0',
    title='test flask',
    description='test flask'
)

api.add_namespace(ns_upload)
api.add_namespace(ns_login)
api.add_namespace(ns_final_upload)
