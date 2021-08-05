#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/4 17:38
# @Author : liu yang
# @Desc: 文件转换保存


import xlrd

from tools.extract_tool import ExtractTool
from tools.index_tool import IndexTool
import pandas as pd
from tools.path_tool import PathTool


class TransTool:

    @staticmethod
    def trans(file, sheet_name, info_cnt):
        """
        :param file: 文件路径
        :param sheet_name: sheet 名称
        :param info_cnt: 基础信息行数
        :return:
        """
        output = pd.DataFrame()

        work_book = xlrd.open_workbook(file)
        sheet_data = work_book.sheet_by_name(sheet_name)

        row_idx, row_cnt = IndexTool.get_row_index(sheet_data, sheet_name, info_cnt)
        start_date, end_date = IndexTool.get_date(sheet_data, sheet_name)

        for idx in range(0, len(row_idx)):
            df_info = pd.read_excel(file,
                                    nrows=1,
                                    sheet_name=sheet_name,
                                    skiprows=row_idx[idx],
                                    header=None)
            work_number, name = ExtractTool.get_info(df_info)

            df_record = pd.read_excel(file,
                                      nrows=(row_cnt[idx]),
                                      sheet_name=sheet_name,
                                      skiprows=(row_idx[idx] + info_cnt),
                                      header=None)

            if df_record.size > 0:
                df_check = ExtractTool.get_record(df_record, start_date, end_date)
            else:
                continue

            for ix, row in df_check.iterrows():
                row_not_null = row[row.notnull()]
                for row_ix, row_value in row_not_null.items():
                    work_time = row[row_ix].split()
                    for time in work_time:
                        dic = {'序号': [work_number],
                               '姓名': [name],
                               '日期': [row_ix],
                               '打卡时间': [time]}
                        output = output.append(pd.DataFrame(dic))

        try:
            output.to_excel(PathTool.out_path(file), index=False)
            print('写入完成')
        except:
            print('文件持久化错误...')


if __name__ == "__main__":
    file_name = '/Users/liuyang/Downloads/员工刷卡记录表（彩云城体验中心）.xls'

