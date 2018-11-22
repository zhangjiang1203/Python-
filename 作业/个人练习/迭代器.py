#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 10:53 AM
# @Author  : zhangjiang
# @Site    : 
# @File    : 迭代器.py
# @Software: PyCharm

'''
迭代器:对于序列类型：字符串、列表、元组，我们可以使用索引的方式迭代取出其包含的元素，但对于字典、集合、文件等类型是没有索引的
若还想取出其内部包含的元素，则必须找出一种不依赖于索引的迭代方式，这就是迭代器

可迭代对象：是指内置有__iter__方法的对象，即obj___iter__,如下
'hello'.__iter__
(1,2,3).__iter__
[1,2,3].__iter__
{"index":3,"name":zhang}.__iter__
{"a","b"}.__iter__

迭代器对象
可迭代对象obj.__iter__() 得到的结果就是迭代器对象
而迭代器对象值的是即内置有__iter__又内置有__next__方法的对象

文件类型是迭代器对象
open('a.txt').__iter__()
open("a.txt").__next__()

迭代器对象一定是可迭代对象，可迭代对象不一定是迭代器对象
'''

dic = {"a":"1","b":"2","c":"3"}
#得到迭代器对象，迭代器对象既有__iter__又有__next__,但是迭代器.__iter__()得到的仍然是迭代器本身
iter_dic = dic.__iter__()
iter_dic.__iter__() is iter_dic #返回的结果就是True
print(iter_dic.__next__())
print(iter_dic.__next__())
print(iter_dic.__next__())
# print(iter_dic.__next__()) #抛出异常StopIteration，或者说结束标志
# 有了迭代器 我们可以不依赖索引索引迭代取值
iter_dic = dic.__iter__()
while 1:
    try:
        k = next(iter_dic)
        print(k)
    except StopIteration:
        break
# 每次这样使用，需要自己捕获异常，自己控制next，更流弊的方式就是使用for循环

#基于for循环，我们可以完全不依赖索引取值
# dic = {"a":"1","b":"2","c":"3"}
# for k in dic:
#     print(k)

'''
for循环的工作原理
#1.执行in后对象的dic.__iter__()方法，得到一个迭代器对象iter_dic
#2.执行next(iter_dic),将得到的值赋值给k，然后执行循环体代码
#3.重复过程2，直到捕捉到异常StopIteration
'''

'''
迭代器的优缺点
优点：
    提供一种统一的、不依赖于索引的迭代方式
    惰性计算、节省内存空间
缺点：
    无法获取长度(只能在next完毕之后才能知道有几个值)
    一次性的，只能往后走，不能回退

'''

str_iter = 'hello'.__iter__()
print(str_iter.__next__())
print(str_iter.__next__())
