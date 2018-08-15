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
from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # include 是一种即插即用的思想，项目根路由不关心具体的app的路由策略，只管往指定的二级路由转发
    # 实现了应用解耦
    path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
]
