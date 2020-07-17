# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 8:33
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : select_tamper.py


import tamper


class tampper():
    """
    @:parameter db_cate 指定数据库类型选择相应的绕过payload
    """
    def __init__(self,db_cate):
        self.db_cate = db_cate

    def select_db_payload(self):

        if not self.db_cate:
            print("[info]将使用sql-tamper 所有的tamper进行内置规则 随机FUZZ bypass尝试....")
            return 0

    def use_tamper(self):
        return tamper.versionedmorekeywords.tamper('')


g = tampper(None).use_tamper()
print(g)