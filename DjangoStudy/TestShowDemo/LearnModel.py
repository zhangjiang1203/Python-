# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:张江

from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

'''
on_delete  字段的说明，下面是其中的几个配置
ASCADE：模拟SQL语言中的ON DELETE CASCADE约束，将定义有外键的模型对象同时删除！（该操作为当前Django版本的默认操作！）
PROTECT:阻止上面的删除操作，但是弹出ProtectedError异常
SET_NULL：将外键字段设为null，只有当字段设置了null=True时，方可使用该值。
SET_DEFAULT:将外键字段设为默认值。只有当字段设置了default参数时，方可使用。
DO_NOTHING：什么也不做。
SET()：设置为一个传递给SET()的值或者一个回调函数的返回值。注意大小写。
'''

'''
通常一个模型映射为一张数据库中的表
每一个字段都是一个类属性，每个类属性表示数据库中的一个列
表名是django自动生成的默认格式为 项目名称 + 下划线 + 小写类名
django默认会自动创建主键

'''

class Fruit(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    #python中手动设置为主键之后，会关闭Django中自动生产id主键的功能，一个模型中只能有一个主键

'''
字段中添加的各种参数
1.choices 设置页面上选着框标签，需要事先提供一个二维的二元元祖，
第一个元素便是存在的数据库内真实的值，第二个表示页面上显示的具体内容
YEAR_IN_SCHOOL_CHOICES= (
    ('FR','FreshMan'),
    ('SO','Sophomore'),
    ('JR','Junior'),
    ('SR','Senior'),
    ('GR','Graduate'),
)
一般的将选项定义在类里面，并取一个直观的名字
'''

class Student(models.Model):
    FRESHMAN = "FR"
    SOPHOMORE = "SO"
    JUNIOR = "JR"
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN,'FreshMan'),
        (SOPHOMORE,'Sophomore'),
        (JUNIOR,'Junior'),
        (SENIOR,'Senior'),
        (GRADUATE,'Graduate'))
    #给当前字段设置可选值和默认值
    year_in_school = models.CharField(max_length=2,choices=YEAR_IN_SCHOOL_CHOICES,default=FRESHMAN)

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR,self.SENIOR)