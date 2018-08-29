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
通常一个模型映射为一张数据库中的表
每一个字段都是一个类属性，每个类属性表示数据库中的一个列

'''