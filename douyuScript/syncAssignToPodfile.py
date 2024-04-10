import os
import sys

# proj_path = os.path.dirname(os.path.abspath(__file__))
#
# print("proj_path =", proj_path)

podfile_path = sys.argv[1]
# podfile_path = "/Users/zhangjiang/Documents/个人项目/douyu/DYHeart/Podfile"


def components_in_line(comps, line):
    for c in comps:
        if line.find("'" + c + "'") != -1:
            return c


def get_component_name(line):
    result = line.split("', :")
    component_name = result[0].split(" '")
    if len(component_name) == 2:
        return component_name[-1]

    return None


def sync_assign_to_podfile():
    components = []
    with open(podfile_path, "r") as file:
        for line in file:
            if line.strip().startswith('#'):
                continue
            # 获取修改之后的组件
            if ":path => " in line or ":git =>" in line:
                # 获取line中的组件名
                component_name = get_component_name(line)
                if component_name is not None:
                    components.append(component_name)

    # 获取该需求中所有涉及的组件后 同步到养鱼工具中
    print(components)
    return components


if __name__ == "__main__":
    sync_assign_to_podfile()
