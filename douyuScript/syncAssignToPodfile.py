import os
import sys

proj_path = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(proj_path, 'syncAssignToPodfile.py')
print("proj_path =", proj_path)


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
    with open(file_path, "r") as file:
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
    return components


if __name__ == "__main__":
    # components = components_in_line(["DYStorage"], "pod 'DYStorage', '0.0.30'")
    # print("hahah", components)
    get_component_name(
        "pod 'Alamofire', :git => 'https://github.com/Alamofire/Alamofire.git', :branch => 'feature_branch'")
    get_component_name("pod 'MyLibrary', :path => '~/Documents/MyLibrary'")
