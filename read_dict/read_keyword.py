# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 13:58
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : read_keyword.py


def get_keywords():

    with open("keyword.txt", "r") as f:
        kb = f.read()
    return kb
