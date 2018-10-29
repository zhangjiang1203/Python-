# 添加装饰器
from django.utils.encoding import python_2_unicode_compatible

import datetime
from django.utils import timezone
from django.db import models

# 添加python2的装饰器
@python_2_unicode_compatible
class Question(models.Model):
    # 字符类型 最大长度200
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # 判断问卷最近是否发布过
    def was_published_recently(self):
        # 限制发布日期在一天以内
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently'


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
'''
  添加了模型之后，我们要启用模型，Django会做下面的两件事，
  1.创建该app对应的数据库表结构
  2.为Question和Choice对象创建基于Python的数据库访问API
  
  启用步骤：
  在项目setting.py文件中查找INSTALLED_APPS字段，配置App路径'polls.apps.PollsConfig'或者直接简写为'polls'
  运行一下以下的命令
  python manage.py makemigrations polls
  告诉Django你对模型有改动，并且想要保存这些改动
  下面的命令就是展示后台执行的sql语句
  python manage.py sqlmigrate polls 0001
  同步数据
  python manage.py migrate
  
  
  在models.py中修改模型；
  运行python manage.py makemigrations为改动创建迁移记录；
  运行python manage.py migrate，将操作同步到数据库

'''


'''
通过python manage.py shell 命令行进入python环境，再执行下面的API

 >>> from polls.models import Question, Choice # 导入我们写的模型类
    # 现在系统内还没有questions对象
    >>> Question.objects.all()
    <QuerySet []>

    # 创建一个新的question对象
    # Django推荐使用timezone.now()代替python内置的datetime.datetime.now()
    # 这个timezone就来自于Django唯一的依赖库pytz
    from django.utils import timezone
    >>> q = Question(question_text="What's new?", pub_date=timezone.now())

    # 你必须显式的调用save()方法，才能将对象保存到数据库内
    >>> q.save()

    # 默认情况，你会自动获得一个自增的名为id的主键
    >>> q.id
    1

    # 通过python的属性调用方式，访问模型字段的值
    >>> q.question_text
    "What's new?"
    >>> q.pub_date
    datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

    # 通过修改属性来修改字段的值，然后显式的调用save方法进行保存。
    >>> q.question_text = "What's up?"
    >>> q.save()

    # objects.all() 用于查询数据库内的所有questions
    >>> Question.objects.all()
    <QuerySet [<Question: Question object>]>
'''

# 添加了解释器之后更改显示的数据
'''
    >>> from polls.models import Question, Choice
    
    # 先看看__str__()的效果，直观多了吧？
    >>> Question.objects.all()
    <QuerySet [<Question: What's up?>]>
    
    # Django提供了大量的关键字参数查询API
    >>> Question.objects.filter(id=1)
    <QuerySet [<Question: What's up?>]>
    >>> Question.objects.filter(question_text__startswith='What')
    <QuerySet [<Question: What's up?>]>
    
    # 获取今年发布的问卷
    >>> from django.utils import timezone
    >>> current_year = timezone.now().year
    >>> Question.objects.get(pub_date__year=current_year)
    <Question: What's up?>
    
    # 查询一个不存在的ID，会弹出异常
    >>> Question.objects.get(id=2)
    Traceback (most recent call last):
    ...
    DoesNotExist: Question matching query does not exist.
    
    # Django为主键查询提供了一个缩写：pk。下面的语句和Question.objects.get(id=1)效果一样.
    >>> Question.objects.get(pk=1)
    <Question: What's up?>
    
    # 看看我们自定义的方法用起来怎么样
    >>> q = Question.objects.get(pk=1)
    >>> q.was_published_recently()
    True
    
    # 让我们试试主键查询
    >>> q = Question.objects.get(pk=1)
    
    # 显示所有与q对象有关系的choice集合，目前是空的，还没有任何关联对象。
    >>> q.choice_set.all()
    <QuerySet []>
    
    # 创建3个choices.
    >>> q.choice_set.create(choice_text='Not much', votes=0)
    <Choice: Not much>
    >>> q.choice_set.create(choice_text='The sky', votes=0)
    <Choice: The sky>
    >>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
    
    # Choice对象可通过API访问和他们关联的Question对象
    >>> c.question
    <Question: What's up?>
    
    # 同样的，Question对象也可通过API访问关联的Choice对象
    >>> q.choice_set.all()
    <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
    >>> q.choice_set.count()
    3
    
    # API会自动进行连表操作，通过双下划线分割关系对象。连表操作可以无限多级，一层一层的连接。
    # 下面是查询所有的Choices，它所对应的Question的发布日期是今年。（重用了上面的current_year结果）
    >>> Choice.objects.filter(question__pub_date__year=current_year)
    <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
    
    # 使用delete方法删除对象
    >>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
    >>> c.delete()

'''