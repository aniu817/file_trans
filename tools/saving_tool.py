#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/16 09:02
# @Author : liu yang
# @Desc:  文件保存


import datetime

from flask import jsonify

import os

from exception.defined_exception import DefinedException
from tools.logging_tool import LoggingTool
from tools.path_tool import PathTool


class SavingTool:
    file_logger = LoggingTool.get_logger(__name__)

    @staticmethod
    def saving_file(file, file_dir):

        file_path = PathTool.get_package_dir(file_dir)
        today = datetime.date.today().strftime('%Y-%m-%d')
        dirs = file_path + '/' + today

        if not os.path.exists(dirs):
            os.makedirs(dirs)

        full_path = dirs + '/' + file.filename

        try:
            file.save(full_path)
            SavingTool.file_logger.info(file.filename + '保存成功...')
            return full_path
        except DefinedException:
            SavingTool.file_logger.error(file.filename + '保存失败...')
            return jsonify({'state': 'false', 'info': '文件上传失败'})
