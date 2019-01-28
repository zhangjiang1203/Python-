#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 2:09 PM
# @Author  : zhangjiang
# @Site    : 
# @File    : manyToManyTable.py
# @Software: PyCharm

from django.db import models
'''
多对多 Django采用的第三张中间表的形式，通过三张表关联manyTomany的关系
'''
class Person(models.Model):
    name = models.CharField(max_length=128)


    def __str__(self):
        '''
        返回Person的打印格式
        :return:
        '''
        return self.name



class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person,through="MemberShip")

    def __str__(self):
        return self.name

'''
中间表示通过id，将两张表关联进行映射
'''
#通过中间模型可以自定义中间表，django提供了一个through参数用户指定中间模型，在上面的group类中添加中间表
class MemberShip(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    date_joined = models.DateField()

    invite_reason = models.CharField(max_length=64)
    '''
    中间表中至少要编写两个外键字段，分别指向关联的两个模型
    '''


ringo = Person.objects.create(name="张胜男")
paul = Person.objects.create(name="lisi")
beatles = Group.objects.create(name="xixian")
m1 = MemberShip.objects.create(person=ringo,group=beatles,date_joined=date(1962,6,17),invite_reason="我就是这么任性")
m1.save()