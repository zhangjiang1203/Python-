import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行API并相应存储
url = 'https://api.github.com/search/repositories?q=language:Swift&sort=stars'
request = requests.get(url)
print("status code",request.status_code)
#将API响应存储在一个变量中
response_dict = request.json()
print("Total repositories :",response_dict['total_count'])

#查看有关仓库信息
repo_dicts = response_dict["items"]
print("Repositories returned:",len(repo_dicts))

#研究第一个仓库
stars_value,name_value = [],[]
for repo_dict in repo_dicts:
    name_value.append(repo_dict['name'])
    #给图表添加自定义的提示 显示这个图表的具体显示内容
    plot_dict = {"value":repo_dict['stargazers_count'],'label':repo_dict['description']}
    stars_value.append(plot_dict)


#对图表进行改进
myStyle = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=myStyle)
chart.title = "Github Sort"
#不需要显示标签 将title设置为''
chart.add('',stars_value)
chart.x_labels = name_value
chart.render_to_file('github.svg')
