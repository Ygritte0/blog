#-*-coding:utf-8-*-
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

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

    def upgrade_battery(self):
        if self.battery_size == 85:
            return None
        else:
            self.battery_size = 85
            print("Your electric car's battery upgrades to 85-kwh.")

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self,battery_size=70):
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


my_Audi = Battery()
my_Audi.get_range()
my_Audi.upgrade_battery()