#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/13 11:41
# @Author : liu yang
# @Desc:


import datetime
import time

from flask import jsonify

import os

from flask_restx import Namespace
from werkzeug.datastructures import FileStorage

from exception.defined_exception import DefinedException
from tools.path_tool import PathTool

from tools.logging_tool import LoggingTool
from flask_restplus import Resource, reqparse
from tools.saving_tool import SavingTool


ns_final_upload = Namespace('final_upload', description='最终文件上传')


@ns_final_upload.route('', strict_slashes=False)
class FinalUpload(Resource):

    file_logger = LoggingTool.get_logger(__name__)

    @staticmethod
    def post():
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=FileStorage, location='files')
        args = parse.parse_args()
        file = args['file']
        if file is None:
            return jsonify({'state': 'false', 'info': '未上传文件'})

        full_path = SavingTool.saving_file(file, 'file')
        return jsonify({'state': 'success', 'info': '完成上传'})

