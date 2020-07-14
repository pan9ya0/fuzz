# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 8:59
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : mysql_keywords.py

import mysql.connector

def con_db():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='sql_fuzz')
    cursor = cnx.cursor()
    query = "select * from reserved_words"
    cursor.execute(query)
    for reserved_word in cursor:
        yield reserved_word
    cnx.close()