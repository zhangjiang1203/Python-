# bicycles = ['trek','cannondale','redline','specialized']
# print(bicycles)
# print(bicycles[0])#列表是有序集合，可以访问他的位置或者索引
# #python为访问最后一个列表元素提供了一个特殊的语法 通过将索引值设置为-1 让python返回最后一个列表元素
# #同理 -2 返回倒数第二个元素 一次类推
# print(bicycles[-1])
# names = ['zhang san','li si','wangwu','zhao liu','lu qi']
# print(names)
# print("你好 " + names[1])
#
# bicycles.append('你好')#添加末尾元素
# print(bicycles)
# bicycles.insert(0,"中国")
# print(bicycles)
# del bicycles[0]
# print(bicycles)
# #pop() 删除列表末尾的元素 并让你能够接着使用它
# last_eleement = bicycles.pop()
# print(bicycles,last_eleement)
# #pop()加上索引可以删除任何位置的数据
# # bicycles.append("支付宝")
# # bicycles.append("微信")
# # print(bicycles)
# # bicycles.remove("微信")
# # print(bicycles)
# #排序 sort()对列表进行永久性排序 默认是按照字母顺序排序的,修改为相反元素的排列顺序时，设置reverse=True
# bicycles.sort(reverse=True)
# #sorted()函数对列表进行临时排序
# print(bicycles)

# placeArr = ['丽江','大理','哈尔滨','新疆','乌鲁木齐','厦门']
placeArr = ['lijiang','dali','haerbin','xinjiang','wulumuqi','xiamen']
print('原始顺序=='+str(placeArr))
# myList = placeArr.sort()
#默认的sorted 是按照字母顺序排序的
# print('sorted排序=='+str(sorted(placeArr,reverse=True)))
placeArr.reverse()
print('反转数组=='+str(placeArr))
placeArr.reverse()
print('再次反转数组=='+str(placeArr))
print('想去地方的个数=='+str(len(placeArr)))
#显示你的数组的个数 len(函数)

#showMsg = []#数组越界
#print(showMsg[-1])