#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/9 14:30
# @Author : liu yang
# @Desc: 文件上传后端接口


import datetime
import time

from flask import Flask, request

import os

from exception.defined_exception import DefinedException
from tools.path_tool import PathTool

from main.entry import Entry
from tools.logging_tool import LoggingTool

app = Flask(__name__)

file_logger = LoggingTool.get_logger(__name__)


@app.route('/upload', methods=['POST', 'GET'])
def upload():

    if request.method == 'POST':
        start = time.time()
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        file = request.files['file']
        if file is None:
            return "未上传文件"

        file_path = PathTool.get_package_dir('input')
        today = datetime.date.today().strftime('%Y-%m-%d')
        dirs = file_path + '/' + today

        if not os.path.exists(dirs):
            os.makedirs(dirs)

        file_name = file.filename
        full_path = dirs + '/' + file_name

        try:
            file.save(full_path)
            file_logger.info(file_name + '保存成功...')
        except DefinedException:
            file_logger.error(file_name + '保存失败...')
            return '文件上传失败'

        try:
            file_logger.info(file_name + '转换开始时间：' + start_time)
            Entry(full_path).run()
        except DefinedException:
            file_logger.error(file_name + '转换失败...')
            return '转换失败，请确认格式...'

        end = time.time()

        file_logger.info(file_name + '完成转换，转换时长为: %f s' % (end - start))

        return '完成转换'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
