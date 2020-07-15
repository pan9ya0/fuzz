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

        if self.path:
            pass
        elif os.path.exists(self.path):
            with open(self.path,'r') as f:
                tmp = f.readline()
                while tmp:
                    yield tmp
                    tmp = f.readline()

        if self.category == "detect":
            with open("SQL2.txt",'r') as f:
                tmp = f.readline()
                while tmp:
                    yield tmp
                    tmp = f.readline()
        if self.category == "exp":
            with open("sql.txt", 'r') as f:
                tmp = f.readline()
                while tmp:
                    yield tmp
                    tmp = f.readline()



# g = get_dict(None,"detect").read_dict1()
# print(next(g))