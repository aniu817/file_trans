#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/8/4 16:23
# @Author : liu yang
# @Desc: 返回考勤行索引、行数

import numpy as np

from tools.logging_tool import LoggingTool


class IndexTool:
    _file_logger = LoggingTool.get_logger(__name__)

    @staticmethod
    def get_row_index(sheet_data,
                      sheet_name,
                      row_num,
                      row_tag='姓'):
        """

        :param sheet_name: sheet 页名称
        :param sheet_data:sheet 页面数据
        :param row_num:基础信息行数
        :param row_tag:基础信息行标签
        :return:
        """
        row_list = []
        total_cnt = sheet_data.nrows
        for idx in range(total_cnt):
            row_data = sheet_data.row_values(idx)
            for value in row_data:
                if row_tag in str(value):
                    row_list.append(idx)

        diff = [row_list[ix + 1] - row_list[ix] for ix in range(len(row_list) - 1)]
        last_row_cnt = total_cnt - row_list[-1]
        diff.append(last_row_cnt)
        if sheet_name == '刷卡记录表':
            row_cnt = (np.array(diff) - row_num - 1).tolist()
        else:
            row_cnt = (np.array(diff) - row_num).tolist()
        row_cnt[-1] = 1 if row_cnt[-1] == 0 or row_cnt[-1] == -1 else row_cnt[-1]
        return row_list, row_cnt

    @staticmethod
    def get_date(sheet_data, name, date_tag='考勤'):
        for idx in range(sheet_data.nrows):
            row_data = sheet_data.row_values(idx)
            date_str = ''.join(row_data)
            date_str = ''.join(date_str.split())
            date_str = date_str.replace('/', '-')
            if date_tag in date_str and len(date_str) > 10:
                if name == '员工刷卡记录表':
                    start_date = date_str[5:15]
                    end_date = date_str[16:26]
                    IndexTool._file_logger.info('开始时间 = ' + start_date + '...结束时间 = ' + end_date)
                    return start_date, end_date
                elif name == '刷卡记录':
                    start_date = date_str[5:15]
                    end_date = date_str[5:9] + '-' + date_str[16:21]
                    IndexTool._file_logger.info('开始时间 = ' + start_date + '...结束时间 = ' + end_date)
                    return start_date, end_date
                elif name == '考勤记录':
                    start_date = date_str[4:14]
                    end_date = date_str[15:25]
                    IndexTool._file_logger.info('开始时间 = ' + start_date + '...结束时间 = ' + end_date)
                    return start_date, end_date
                elif name == '刷卡记录表':
                    start_date = date_str[5:15]
                    end_date = date_str[5:9] + '-' + date_str[16:21]
                    IndexTool._file_logger.info('开始时间 = ' + start_date + '...结束时间 = ' + end_date)
                    return start_date, end_date


if __name__ == "__main__":
    pass

