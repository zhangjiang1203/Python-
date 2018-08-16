from django.shortcuts import render,get_object_or_404
#404 模块显示问题
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
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
    # response = "You're looking at the result of question %s"
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{"question":question})

def vote(request,question_id):
    '''
    投票的选项
    :param request:
    :param question_id:
    :return:
    '''
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        #发生choice未找到异常时，重新返回表单页面，并给出提示信息
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You don't select a choice",
        })
    else:
        selected_choice.votes += 1
        # 保存信息
        selected_choice.save()
    # 返回一个重定向的URL
    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))