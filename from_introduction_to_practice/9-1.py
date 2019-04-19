#-*-coding:utf-8-*-
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name.title() + '.')
        print("We have " + self.cuisine_type + ' food.')

    def open_restaurant(self):
        print("Our restaurant is opening . Welcome!")


my_restaurant = Restaurant('湖南小炒肉','hunan')
your_restaurant = Restaurant('粤菜馆','guangdong')
the_restaurant_in_corner = Restaurant('门框卤煮火烧','beijing')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

the_restaurant_in_corner.describe_restaurant()
the_restaurant_in_corner.open_restaurant()