#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 9:40 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : 01-reCalculateTest.py
# @Software: PyCharm
import re


def exec_bracket(express):
    # 递归处理展示事件
    #判断表达式中是否有括号,直接拿出其中的表达式开始计算
    if not re.search('\(\)',express):
        return None







if __name__ == "__main__":
    inpp = "1-2*(3.78-45*(2/4-0.7))+56*(23-79/4)"
    #替换掉所有的空白字符 等价于[\t\n\r\f]
    inpp = re.sub("\s*",'',inpp)
    #获取表达式
    result = exec_bracket(inpp)
    print(result)
