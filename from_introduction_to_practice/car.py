#-*-coding:utf-8-*-
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

# 通过方法修改属性的值
    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值，禁止将里程表读数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        """将里程表增加指定的量"""
        """禁止回调里程表"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

# my_used_car = Car('subaru','outback', 2013)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(-2)
# my_used_car.read_odometer()

# my_new_car = Car('audi','a4','2016')
# print(my_new_car.get_descriptive_name())
#直接修改属性的值
# my_new_car.odometer_reading = 23
# 通过方法修改属性的值
# my_new_car.update_odometer(25)
# my_new_car.read_odometer()


