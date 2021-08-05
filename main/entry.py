#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/4 16:12
# @Author : liu yang
# @Desc: 程序入口
import xlrd
from tools.trans_tool import TransTool


class Entry:

    def __init__(self, file):
        self.file = file

    def run(self):
        work_book = xlrd.open_workbook(self.file)
        sheet_name = work_book.sheet_names()
        for name in sheet_name:
            name = name.strip()
            if name == '员工刷卡记录表':
                TransTool.trans(self.file, name, 2)
            elif name == '刷卡记录':
                TransTool.trans(self.file, name, 1)
            elif name == '考勤记录':
                TransTool.trans(self.file, name, 1)
            elif name == '刷卡记录表':
                TransTool.trans(self.file, name, 1)


if __name__ == "__main__":
    file_name = '/Users/liuyang/Downloads/员工刷卡记录表（彩云城体验中心）.xls'
    Entry(file_name).run()
