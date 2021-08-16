# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time : 2021/8/5 08:22
# # @Author : liu yang
# # @Desc: 注册蓝图


from flask import Flask


def create_app():
    # 创建Flask对象
    app = Flask(__name__)
    # 注册蓝图
    from app.user.api import api_user
    app.register_blueprint(api_user)
    return app
