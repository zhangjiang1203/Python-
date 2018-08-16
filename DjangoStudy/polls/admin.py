from django.contrib import admin

# 引入站点
from .models import Question
# 注册站点应用，注册之后刷新就可以看到对应的模块了
admin.site.register(Question)