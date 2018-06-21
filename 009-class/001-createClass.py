class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title()+ " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " roller over!")


myDog = Dog("lisi",17)
print("my dog name is " + myDog.name.title() + ".")
print("my dog is "+str(myDog.age) + " year old")
myDog.sit()
myDog.roll_over()

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("restanrant's name is "+self.restaurant_name.title())
        print("cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
         print("餐馆正在营业 ")

myRestaurant = Restaurant("张三的小吃店",'小吃')
myRestaurant.describe_restaurant()
myRestaurant.open_restaurant()


class Car():

    gender = "Man"
    def __init__(self,make,model,year):
        self.make = make
        self.model =  model
        self.year = year
        self.odometer_reading = 0

    def get_description_name(self):
        long_name = str(self.year)+' '+self.make+ " " +self.model
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

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_description_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 100
my_new_car.read_odometer()
my_new_car.update_odometer(99)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()

#继承
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("this car doesn't need a gas tank")

my_tesla = ElectricCar("tesla","model s",2017)
my_tesla.fill_gas_tank()
print(my_tesla.get_description_name())

# 增加对象引用计数的场景
# 1.对象创建
# 2.将对象添加进容器
# 3.对象被当做参数传递给函数
# 4.为对象创建另外的变量名

# 减少引用计数
# 1.引用此对象的某些变量名被显示销毁 如 del x
# 2.给引用此对象的某变量名重新赋值
# 3.从容器中移除对象时，类似 list.pop()
# 4.容器本身被销毁时


'''
继承至父类，覆盖父类的方法时，不显式调用父类的方法，子类没法访问覆盖方法中定义的属性值
'''
class ParentClass():
    def createname(self,age = 'sex'):
        self.age = age

class subClass(ParentClass):
    def createname(self,age):
        self.name = age
        ParentClass.createname(self)


sub = subClass()
sub.createname(18)
print(sub.age)