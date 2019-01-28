#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 2:42 PM
# @Author  : zhangjiang
# @Site    : 
# @File    : 模型的元数据Meta.py
# @Software: PyCharm

from django.db import models

class Ox(models.Model):

    horn_length = models.IntegerField()

    #模型的元数据指的就是除了字段外的所有内容，例如排序方式、数据表名等
    #模型中添加元数据 就是在模型中添加一个子类，名字是固定的Meta，然后再这个子类中增加各种元数据或者说是设置项
    class Meta: #这个是模型的子类，一定要缩进
        ordering = ['horn_length']
        verbose_name_plural = "oxen"
        order_with_respect_to = 'question'
    #我们为Ox类添加了两个元数据，分别表示排序和复数名,order_with_respect_to字段是根据指定的字段进行排序
    #ording是最常用的一个元数据之一，用于指定该模型生成的所有对象的排序，若是在字段名前面加上- 则表示按着降序返回 使用? 表示随机返回