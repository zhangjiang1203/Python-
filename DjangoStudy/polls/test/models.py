#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-17 15:56
# @Author  : zhangjiang
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from showModels import Blog

b = Blog(name="beatles Blog",tagline="all the latest beatles news")
b.save()
# 一步完成这个操作，可以使用create()方法去创建，可以省略save的步骤