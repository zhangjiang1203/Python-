#python将不能修改的值称为不可变的，而不可变的列表被称为元祖
dimensions = (200,300)
print(dimensions)
#修改dimensions中的一个值 这样会直接报错
#dimensions[0]= 400
for dimension in dimensions:
    print(dimension)
#虽然不能修改元祖的元素，但可以给存储元祖的变量赋值，若要修改元祖元素，可以重新定义整个元祖
dimensions = (400,500)
print(dimensions)

