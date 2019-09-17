#-*-coding:utf-8-*-
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("User's name is " + self.first_name.title() + ' ' + self.last_name.title() +  '.')

    def greet_user(self):
        print("Hello, " + self.first_name.title() + ' '+ self.last_name.title() + '.')


class Privileges():
    def __init__(self):
        privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = privileges

    def show_privileges(self):
        for x in self.privileges:
            print(x)

class Admin(User):
    def __init__(self):
        super(Admin, self).__init__(first_name='eric', last_name='green')
        privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = privileges


John = Privileges()
John.show_privileges()
