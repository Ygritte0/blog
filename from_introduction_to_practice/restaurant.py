#-*-coding:utf-8-*-
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

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