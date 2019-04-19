#-*-coding:utf-8-*-
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("User's name is " + self.first_name.title() + ' ' + self.last_name.title() +  '.')

    def greet_user(self):
        print("Hello, " + self.first_name.title() + ' '+ self.last_name.title() + '.')


user = User("william",'smith')
user_2 = User('tom','green')
user_3 = User('sam','tully')

user.describe_user()
user.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()