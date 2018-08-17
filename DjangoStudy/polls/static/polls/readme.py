# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:张江

'''

1.使用静态文件
  首先在对应的App中创建一个static目录，Django将在这里查找静态文件，这与Django在app/template/中查找对应的模板方式是一致的
  Django的STATICFILES_FINDERS设置项目中包含一个查找器列表，他们知道如何从各种资源中找到静态文件，其中的一个默认查找器是
  AppDirectoriesFinder，它是在Installed_apps下下查找static子目录，

  在刚创建的static目录中新建一个polls子目录，再在该子目录中创建一个style.css文件，

  静态文件的命名空间：

    与模板类似，我们可以将静态文件直接放在polls/static（而不是创建另外一个polls 子目录），但实际上这是一个坏主意。
    Django将使用它所找到的第一个匹配到的静态文件，如果在你的不同应用中存在两个同名的静态文件，Django将无法区分它们。
    我们需要告诉Django该使用其中的哪一个，最简单的方法就是为它们添加命名空间。
    也就是说，将这些静态文件放进以它们所在的应用的名字同名的另外一个子目录下（白话讲：多建一层与应用同名的子目录）。

    PS：良好的目录结构是每个应用都应该创建自己的urls、views、models、templates和static，
    每个templates包含一个与应用同名的子目录，每个static也包含一个与应用同名的子目录。

'''