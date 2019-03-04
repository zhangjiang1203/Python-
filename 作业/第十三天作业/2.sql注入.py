#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-04 10:59
# @Author  : zhangjiang
# @Site    : 
# @File    : 2.sql注入.py
# @Software: PyCharm


import pymysql

# 拿到用户输入的行号和密码进行登录

name = input("请输入账号:").strip()
password = input("请输入密码:").strip()




# 连接mysql,注意字符编码(utf8,不要加中划线)和端口号设置(端口号为数字)
# 添加参数之后可以返回执行的数组嵌套字典的格式
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='zj901203',
                       database='schoolInfo',
                       port=3306,charset='utf8',
                       # cursorclass 设置返回的格式为数组套字典，不设置返回的就是元组套元组
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()

#查找数据库是否有这个人
# 返回的是结果的个数
# res = cursor.execute('select * from users')#' where uname=%s and upwd=%s' %(name,password))
# 添加条件的时候 sql语句 中的%s加单引号 一定要记得
# sql直接拼接会造成sql注入的bug，项目中不要使用这种方式
# 用户传过来的数据不能直接拼接
# count = cursor.execute("select * from users where uname='%s' and upwd='%s'" %(name,password))

# 使用下面的方式执行sql语句
sql = "select * from users where uname=%s and upwd=%s"
cursor.execute(sql,(name,password))
res = cursor.fetchall()
if res:
    print("登录成功")
else:
    print("用户不存在")



# -- create view v1
# -- as
# -- SELECT * FROM users;
#
# -- 创建视图 ，直接使用别名查询对应的数据，这样可以设置对应的权限使用
# -- 视图是虚拟的，不是真实存在的，往视图中添加数据的时候会报错
#
# SELECT * from v1;



