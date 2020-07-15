# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 14:59
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : user_agent.py

import random

"""
随机ua 接口
@:return 一个随机UA字符串
"""
def get_header():

    # rand = random.choice(User_Agent)
    # return {"User-Agent":rand}
    with open("UA.txt",'r') as f:
        user_agent = f.readlines()

        ua = random.choice(user_agent)
        return ua