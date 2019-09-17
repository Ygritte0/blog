#-*-coding:utf-8-*-
from car import Car
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' +  self.model
        return long_name.title()

    def read_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

    def fill_gas_tank(self,litre):
        self.litre = litre
        return litre

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

    def __init__(self,make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


    # def fill_gas_tank(self):
    #     print("This car doesn't need a gas tank!")
    #     print("=============")

my_tesla = ElectricCar('tesla','model s','2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
my_tesla.battery.get_range()