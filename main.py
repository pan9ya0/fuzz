# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 21:50
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : main.py


import fuzz
import sys
from read_dict import read_dict
import param_handle
from read_dict import from_db_read
import create_payload


def main():
    a = sys.argv
    """
    单个单词或符号fuzz
    """

    # g = read_dict.read_dict(None, "detect").read_dict1()
    # payload = next(g)
    # try:
    #     while payload:
    #         print(payload)
    #         payload = next(g)
    # except Exception as e:
    #     pass
    """
    关键字fuzz
    """
    deform_payload = create_payload.create_payload()
    g = from_db_read.con_db()
    payload = next(g)

    try:
        while payload:
            print(deform_payload.high_low_deform(payload))
            payload = next(g)
    except Exception as e:
        pass

    # url = get_url()
    # payload = payload()
    # for i in payload:
    #     if len(url) > 1:
    #         for i in url:
    #             fuzz(i,url)
    #print(a)


if __name__ == '__main__':
    main()
