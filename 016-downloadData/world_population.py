from country_code import get_country_code
import json
import pygal
#引入地图的一种基色
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle


def get_world_person():
    file_name = "population_data.json"
    try:
        with open(file_name) as obj:
            data = json.load(obj)
    except FileNotFoundError:
        print("文件不存在")
        return None
    else:
        cc_populations = {}
        for pop in data:
            if pop['Year'] == '2010':
                country_name = pop['Country Name']
                country_code = get_country_code(country_name)
                country_pop = int(float(pop['Value']))
                if country_code:
                    cc_populations[country_code] = country_pop
                else:
                     print("Error - " + country_name)

        return cc_populations


def draw_population_map():
    #拿到人口数据
    pop_data = get_world_person()
    #根据人口数量将所有的国家分成三个等级
    cc_pop1,cc_pop2,cc_pop3 = {},{},{}
    for cc,pop in pop_data.items():
        print(pop)
        if int(pop) < 10000000:
            cc_pop1[cc] = pop
        elif pop < 100000000:
            cc_pop2[cc] = pop
        else:
            cc_pop3[cc] = pop

    #给地图添加一个基色
    wy_style = RotateStyle('#336699',base_style=LightColorizedStyle)
    wm = pygal.maps.world.World(style=wy_style)
    wm.title = "2010年世界人口"
    wm.add('0-10m',cc_pop1)
    wm.add('10m-1bn',cc_pop2)
    wm.add('>1bn',cc_pop3)
    wm.render_to_file('world_population.svg')


draw_population_map()