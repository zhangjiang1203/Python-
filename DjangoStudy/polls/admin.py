from django.contrib import admin

# 引入站点
from .models import Question, Choice


# 注册站点应用，注册之后刷新就可以看到对应的模块了,不注册是看不到对应的app的
#admin.site.register(Question)


# 同时在新建question的时候加上choice
# 列表排列 admin.TabularInline   纵队排列 admin.StackedInline
class ChoiceInline(admin.TabularInline):
    # 设置的模型
    model = Choice
    # 添加几个关联对象
    extra = 3

# 定制模型表单
class QuestionAdmin(admin.ModelAdmin):
    # 设置各个字段在站点上显示的顺序,这个是不分区域显示
    # fields = ['pub_date','question_text']
    # 显示Question中的每一个字段
    list_display = ('question_text','pub_date','was_published_recently')
    # 对显示的结果进行过滤,按着时间开始过滤
    list_filter = ['pub_date']
    # 添加搜索面板根据question_text进行搜索
    search_fields = ['question_text']


    #对于多个字段，想要将表单划分为一些字段的集合的时候修改fields
    fieldsets = [
        (None,              {'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)