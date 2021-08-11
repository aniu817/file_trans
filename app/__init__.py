#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/5 08:22
# @Author : liu yang
# @Desc: 注册蓝图


from flask import Flask

from app.user.upload import upload_bp
from app.user.login import login_bp

my_flask = Flask(__name__)

my_flask.register_blueprint(upload_bp)
my_flask.register_blueprint(login_bp)
