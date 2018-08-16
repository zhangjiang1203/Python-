from django.shortcuts import render
#404 模块显示问题
from django.http import HttpResponse,Http404
from .models import Question
# from django.template import loader

'''
下面定义的每一个方法就是一个视图，包含index detail results vote 这四个视图
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    # return HttpResponse(template.render(context,request))
    #使用render函数一部到位render()函数的第一个位置参数是请求对象（就是view函数的第一个参数），
    # 第二个位置参数是模板。还可以有一个可选的第三参数，一个字典，
    # 包含需要传递给模板的数据。
    # 最后render函数返回一个经过字典数据渲染过的模板封装而成的HttpResponse对象。
    return render(request,'polls/index.html',context)



def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request,'polls/detail.html',{"question":question});
    # return HttpResponse("You're looking at question %s." %question_id)


def results(request,question_id):
    response = "You're looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." %question_id)