#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-04 09:36
# @Author  : zhangjiang
# @Site    : 
# @File    : 1.python操作mysql.py
# @Software: PyCharm

import pymysql

# 连接mysql,注意字符编码(utf8,不要加中划线)和端口号设置(端口号为数字)
# 添加参数之后可以返回执行的数组嵌套字典的格式
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='zj901203',
                       database='gushici_data',
                       port=3306,charset='utf8',
                       # cursorclass 设置返回的格式为数组套字典，不设置返回的就是元组套元组
                       cursorclass=pymysql.cursors.DictCursor)
# 拿到游标执行sql语句
cursor = conn.cursor()
# 执行sql语句
res = cursor.execute("select * from Author")
# cursor.fetchone() #只拿一个
# cursor.fetchmany(size=10)  拿十条数据

info = cursor.fetchall() #返回的是元组
print(info)
# 添加单个数据
# cursor.execute("insert into student (sname,gender,class_id) values (%s,%s,%s)" %('你好','男',2))
# 添加多个数据
# cursor.executemany("insert into student (sname,gender,class_id) values (%s,%s,%s)", [('你好1','男',1),('你好2','男',5),('你好3','男',6)])
# 这个里面是默认开启事务的 删除 更新 新增的时候都要调用commit

# 删除和更新也是类似的操作

# 获取数据库中最后一条数据的id是多少
print(cursor.lastrowid)


# conn.commit()


# 最后关闭数据库
cursor.close()
conn.close()