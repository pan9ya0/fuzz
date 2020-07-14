# encoding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 21:50
# @Author  : Pan9ya0
# @Email   : su33e7@gmail.com
# @File    : main.py

"""
@version：0.1
功能：
TODO:调用fuzz常见参数名框架，对参数值进行fuzz，发现注入点；

framework的目标：找出CTF中的未过滤字符，以及发现可以bypass waf 的payload及规则，fuzz 变形，
能够自动生成tamper，调用sqlmap；

注意：不要和sqlmap有功能重合！！！

设计理念：参考wfuzz

字典:
ALL:
    1.所有可打印字符字典
    2.所有常见的payload
    3.各种数据库的关键词
    4.
Mysql：
    1.大小写变换

流程：

TODO:0. 注入点(参数)发现：请求包；url中的GET/POST参数；常见的HTTP字段或
1. 手工标注：注入点
2.5 是否设置代理ip池
    --proxy=http://127.0.0.1:5320

2. 根据fuzz规则及模式设置，读取相应字典或自定义字典
3.0 根据设置的规则，对读取的字典进行变形
    变形规则：对sql注入语句中常见的符号和关键字执行，先尝试替换再 编码变形
    1.通用tamper 替换
    2.

3. 根据设置的线程数，多线程发包
4. 对响应内容根据设置的规则进行保存及处理：根据相应的长度，保存相应内容，响应时间

5. 根据第四步的判断，输出到屏幕和本地文件 原payload-----变形后的payload，

对发现的注入点，进行fuzz注入：读取字典，第一遍原始fuzz，查看未过滤的普通字符；
    第二遍，进行常规变形，对字符进行
    =-PJN各种编码，
    变形的顺序：替换--->编码---->misc替换
    替换：sqlmap-tamper；指定数据库，不指定数据库默认全部进行测试
    编码：
    final处理：进行url编码，对一些浏览器无法传输的符号进行编码 空格%20

    替换：

参数介绍：
web 请求的两种方式，注入点放入”FUZZ,FUZ2Z,FUZ3Z,.....FUZNZ"：
    指定请求文件          -req 请求文件
    指定url              -u url，--data 指定POST类型数据

选择进行注入测试的类型/场景的payload：(这个可以通过简单的人工经验分析)
    default: 全部场景 payload fuzz，包括各种数据库，各种功能场景或功能点，
    1.联合查询
    2.报错注入      适用情况：联合查询受限且能返回错误信息的情况。对响应长度进行记录
    3.布尔盲注
    4.时间盲注
    5.HTTP头注入
    6.HTTP分割注入
    7.二次注入
    8.SQL约束攻击

选择进行的fuzz规则：
    -fN 正常对payload进行尝试：url编码，浏览器编码，16进制编码
    -fS 使用常见的sqltamper 规则进行fuzz , all mssql,mysql
    -fR

TODO:
    -T：自动化调用参数字典，进行sql-fuzz
"""

import fuzz
import sys
from read_dict import read_dict
import param_handle

def main():
    # a = sys.argv
    """
    单个单词或符号fuzz
    :return:
    """

    g = read_dict.read_dict(None, "detect").read_dict1()
    payload = next(g)
    try:
        while payload:
            print(payload)
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
