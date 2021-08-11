#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/5 13:19
# @Author : liu yang
# @Desc: 手动运行文件转换
import os

from main.entry import Entry

dirs = '/Users/liuyang/PycharmProjects/file_trans/input/2021-08-10'

for root, dirs, files in os.walk(dirs):
    for file in files:
        file_name = root + '/' + file
        print(file_name)
        if 'DS' in file_name:
            continue
        Entry(file_name).run()
