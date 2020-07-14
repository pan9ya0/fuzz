# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 22:08
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : create_payload_rules.py


class payloadsRules:
    """
    根据读取的用户传入的sys参数，进行生成fuzz payloads规则

    """
    def __init__(self,sqlmap_tamper):
        self.sqlmap_tamper =sqlmap_tamper