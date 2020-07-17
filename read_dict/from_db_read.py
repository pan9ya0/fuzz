# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 8:59
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : from_db_read.py

import mysql.connector

def con_db():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='sql_fuzz')
    cursor = cnx.cursor()
    query = "select reserved_word from reserved_words"
    cursor.execute(query)
    for (word) in cursor:
        yield word[0]

    cnx.close()


