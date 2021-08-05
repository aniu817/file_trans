#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/5 10:45
# @Author : liu yang
# @Desc: 日志操作

import logging
import os

from tools.path_tool import PathTool
import datetime


class LoggingTool:

    _log_name = 'run.log'
    _format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        # fh = self._file_handler()
        fh = logging.FileHandler(LoggingTool._get_log_path())
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter(LoggingTool._format))
        logger.addHandler(fh)
        return logger

    @staticmethod
    def _get_log_path():
        path = PathTool.get_package_dir('log')
        today = datetime.date.today().strftime('%Y-%m-%d')
        dirs = path + '/' + today

        if not os.path.exists(dirs):
            os.makedirs(dirs)
        return dirs + '/' + LoggingTool._log_name


if __name__ == "__main__":
    pass
