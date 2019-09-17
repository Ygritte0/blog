#-*-coding:utf-8-*-
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.flavors = ['strawberry','mango','chocolate','milk','orange','banana']

    def describe_restaurant(self):
        # print("This restaurant's name is " + self.restaurant_name.title() + '.')
        # print("We have " + self.cuisine_type + ' food.')
        # print("We have " + str(self.number_served) + ' guests served.')
        msg = self.name + " serves wonderful " + self.cuisine_type + '.'
        print(msg)

    def open_restaurant(self):
        # print("Our restaurant is opening . Welcome!")
        msg = self.name + ' is open.Come on in!'
        print(msg)

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,additional_served):
        self.number_served += additional_served

    def ice_cream_flavors(self,flavors):
        self.flavors = flavors
        print("Which flavor of the ice cream would you like? We have flavors as following:")
        flavors = ['strawberry','mango','chocolate','milk','orange','banana']
        for x in flavors:
            print(x)
        choosed_flavor = input("Just tell me:")
        print("OK! I will make a %s ice cream for you!" % choosed_flavor)


IceCreamStand = Restaurant('Milky','ice cream')
IceCreamStand.ice_cream_flavors(None)
