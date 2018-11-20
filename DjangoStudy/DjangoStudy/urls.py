"""DjangoStudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # include 是一种即插即用的思想，项目根路由不关心具体的app的路由策略，只管往指定的二级路由转发
    # 实现了应用解耦
    url(r'^polls/',include('polls.urls')),
    url(r'^my/set/', admin.site.urls),
]
'''
在实际环境中，为了站点的安全性，我们不能将管理后台的url随便暴露给他人，不能用/admin/这么简单的路径。

DjangoStudy/urls.py，修改其中admin.site.urls对应的正则表达式，换成你想要的，比如：

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^my/set/', admin.site.urls),
]
这样，我们必须访问http://127.0.0.1:8000/my/set/才能进入admin界面。
'''

