#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/9 14:30
# @Author : liu yang
# @Desc: 文件上传后端接口
from app import create_app

my_flask = create_app()

if __name__ == '__main__':
    print(my_flask.url_map)
    my_flask.run(host='0.0.0.0')

