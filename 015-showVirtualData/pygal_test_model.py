import pygal
from random import randint

def get_random_num():
    results = []
    for value in range(1,12):
        results.append(randint(200,1001))
    return results

#绘制线段d
line_chart = pygal.Line()
line_chart.title = "显示的大标题"
#设置了x_labels 绘制饼状图的时候不显示圆环半径
line_chart.x_labels = map(str,range(2002,2013))
line_chart.add("random1",get_random_num())
line_chart.add("random2",get_random_num())
line_chart.add("random3",get_random_num())
line_chart.add("random4",get_random_num())
line_chart.render_to_file("pygal_test.svg")

