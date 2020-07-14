# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 11:43
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : param_handle.py


class params_handle:
    def __init__(self):
        params_length = len(self)

        for i in range(params_length):
            if self[i] == "-u":
                print("url为{}".format(self[i + 1]))
            if self[i] == "-d":
                print("默认模式 不猜测数据库和版本，全payloads模式")
            if self[i] == "-E":
                print("带外平台 需要进行进一步配置")


    def handle_param(params):

        params_length = len(params)

        for i in range(params_length):
            if params[i] == "-u":
                print("url为{}".format(params[i+1]))
            if params[i] == "-d":
                print("默认模式 不猜测数据库和版本，全payloads模式")
            if params[i] == "-E":
                print("带外平台payload设置 需要进行进一步配置")

        return
