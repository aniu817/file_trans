#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/11 11:59
# @Author : liu yang
# @Desc: 文件转换


from flask import Blueprint

import datetime
import time

from flask import Flask, request

import os

from werkzeug.datastructures import FileStorage

from exception.defined_exception import DefinedException
from tools.path_tool import PathTool

from main.entry import Entry
from tools.logging_tool import LoggingTool
from flask_restful import Resource, reqparse


class Upload(Resource):

    file_logger = LoggingTool.get_logger(__name__)

    @staticmethod
    def post():
        start = time.time()
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=FileStorage, location='files')
        args = parse.parse_args()
        file = args['file']
        if file is None:
            return "未上传文件"

        file_path = PathTool.get_package_dir('input')
        today = datetime.date.today().strftime('%Y-%m-%d')
        dirs = file_path + '/' + today

        if not os.path.exists(dirs):
            os.makedirs(dirs)

        full_path = dirs + '/' + file.filename

        try:
            file.save(full_path)
            Upload.file_logger.info(file.filename + '保存成功...')
        except DefinedException:
            Upload.file_logger.error(file.filename + '保存失败...')
            return '文件上传失败'

        try:
            Upload.file_logger.info(file.filename + '转换开始时间：' + start_time)
            Entry(full_path).run()
        except DefinedException:
            Upload.file_logger.error(file.filename + '转换失败...')
            return '转换失败，请确认格式...'

        end = time.time()

        Upload.file_logger.info(file.filename + '完成转换，转换时长为: %f s' % (end - start))

        return '完成转换'
