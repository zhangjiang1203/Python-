#导入一个模块的中的多个类
from myCar import Car,Restaurant

my_new_car = Car("zhangsan","nihao",1990)
print(my_new_car.get_description_name())

# from 001-createClass import Car
# my_new_car = Car("zhangsan","nihao",1990)
# print(my_new_car.get_description_name())


my_hotel = Restaurant("我的餐厅","小吃")
my_hotel.describe_restaurant()