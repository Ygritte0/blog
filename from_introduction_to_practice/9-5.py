#-*-coding:utf-8-*-
class User():
    def __init__(self, first_name, last_name):
        # 像self.first_name = first_name 这样可以通过实例访问的变量称为属性！
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("User's name is " + self.first_name.title() + ' ' + self.last_name.title() +  '.')

    def greet_user(self):
        print("Hello, " + self.first_name.title() + ' '+ self.last_name.title() + '.')

    def increments_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0



user1 = User('Judy','Green')
user2 = User('tom','smith')
user3 = User('bran','stark')
user1.increments_login_attempts()
user1.increments_login_attempts()
user1.increments_login_attempts()
user3.increments_login_attempts()
print("Login attempts: " + str(user1.login_attempts))
print("Login attempts: " + str(user3.login_attempts))

user1.reset_login_attempts()
print("Login attempts: " + str(user1.login_attempts))

