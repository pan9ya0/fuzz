# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 22:08
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : create_payload.py

import random
import re
class create_payload:
    """
    通用变换
    1.对单词关键字进行大小写变换, 针对大小写不敏感的sql语句
    """
    def __init__(self):
        # self.payload = payload
        pass
    def high_low_deform(self, payload):

        payload = payload
        try:
            if payload.isupper():
                length = len(payload)
                num = random.randint(0, length-1)
                payload = payload[:num]+payload[num].lower()+payload[num+1:]
                return payload
            elif payload.islower():
                length = len(payload)
                num = random.randint(0, length-1)
                payload = payload[:num]+payload[num].upper()+payload[num+1:]
                return payload
            else:
                return payload

        except Exception as e:
            print("非全大写或小写payload")


    """
    根据不同数据库对特殊字符的替换
    对注入检测sql语句进行判断
    """
    # def multiplespaces(self, payload):
    #     return

    def multiplespaces(payload, **kwargs):

        retVal = payload

        if payload:
            words = set()

            for match in re.finditer(r"[A-Za-z_]+", payload):
                word = match.group()

                if word.upper() in kb.keywords:
                    words.add(word)

            for word in words:
                retVal = re.sub("(?<=\W)%s(?=[^A-Za-z_(]|\Z)" % word,
                                "%s%s%s" % (' ' * random.randrange(1, 4), word,
                                            ' ' * random.randrange(1, 4)),
                                retVal)
                retVal = re.sub("(?<=\W)%s(?=[(])" % word,
                                "%s%s" % (' ' * random.randrange(1, 4), word),
                                retVal)

        return retVal
# a = input("input")
# while a:
#     g = create_payload(a)
#     print(g.high_low_deform())
#     a = input("input")