## 安装之前最好确认已经安装好Python
开发工具为pycharm，Pycharm不但是Python最好的集成环境，并且对Django、Flask、HTML5等各种框架和语言都非常友好

### Django的安装
#### 1.命令行安装
```shell
#自动安装pypi提供的最新版本
pip install django

#安装指定版本
pip install django==1.10这种形式
```
#### 2.验证安装
 在Python交互式模式下
```shell
>>> import django
>>> print(django.get_version())
1.11
```

#### 3.创建django项目
```shell
django-admin startproject mysite
```
这样会在当前目录下创建一个mysite的Django项目,使用tree命令查看结构
```shell
.
|____mysite
| |______init__.py
| |____settings.py
| |____urls.py
| |____wsgi.py
|____manage.py
```

在项目根目录下，运行```Python manage.py runserver```，Django会以127.0.0.1:8000这个默认配置启动开发服务器。