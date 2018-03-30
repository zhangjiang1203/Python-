import pygal
from pygal.style import LightenStyle as LS,LightColorizedStyle as LCS

my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title = "my Project"
chart.x_labels = ['httpie','django','flask']

plot_dicts = [{'value':17800,'label':'Description of httpie'},
              {'value':13867,'label':'Description of django'},
              {'value':15389,'label':'Description of flask'}]

chart.add('',plot_dicts)
chart.render_to_file('custom.svg')