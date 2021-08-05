#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/4 18:31
# @Author : liu yang
# @Desc:  提取 EXCEL 数据信息

import pandas as pd


class ExtractTool:

    @staticmethod
    def get_info(df_info):
        """
        :param df_info:只取工号、姓名、公司那一行的数据
        :return:返回工号、姓名
        """
        df_info.dropna(axis=1, how='any', inplace=True)
        df_info.columns = list(range(len(df_info.columns)))

        try:
            return df_info.iloc[0][1], df_info.iloc[0][3]
        except:
            print('姓名为空')
            return '', ''

    @staticmethod
    def get_record(df_record, start_date, end_date, mode='%Y%m%d'):
        """

        :param start_date: 开始日期
        :param end_date: 结束日期
        :param df_record: 取序号以及考勤数据行
        :param mode: 格式为 YYYYMMDD
        :return: 返回打卡记录以及对应的日期
        """
        col_cnt = pd.date_range(start_date, end_date).size
        df_record = df_record.iloc[:, :col_cnt]
        df_record.columns = pd.date_range(start_date, end_date)
        df_record.columns = df_record.columns.to_series().apply(lambda x: x.strftime(mode))
        return df_record
