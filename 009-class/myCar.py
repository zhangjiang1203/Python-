class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model =  model
        self.year = year
        self.odometer_reading = 0

    def get_description_name(self):
        long_name = str(self.year)+' '+self.make+" "+self.model
        return long_name.title()

    def read_odometer(self):
        print("this car has "+str(self.odometer_reading) + " miles on it")

    """通过方法修改属性的值"""
    def update_odometer(self,mile):
        """禁止将里程表读数设置为指定的值"""
        if mile >= self.odometer_reading:
            self.odometer_reading = mile
        else:
            print("你不能回滚里程表数")
    def fill_gas_tank(self):
        print("开始给汽车加油")

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("restanrant's name is "+self.restaurant_name.title())
        print("cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
         print("餐馆正在营业 ")