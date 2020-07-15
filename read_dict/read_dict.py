# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 10:48
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : read_dict.py

import os

class read_dict:
    """
    path：自定义字典路径
    category：字典类型：探测型 detect，利用型 exp
    """
    def __init__(self,path, category):
        self.path = path
        self.category = category

    def read_dict1(self):

        if self.path == None:
            pass
        elif os.path.exists(self.path):
            read_txt(path)

        if self.category == "detect":
            read_txt("SQL2.txt")
        if self.category == "exp":
            read_txt("sql.txt")


def read_txt(self,path):
    with open(path, 'r') as f:
        tmp = f.readline()
        while tmp:
            yield tmp
            tmp = f.readline()

g = read_dict(None,"detect").read_dict1()
print(next(g))