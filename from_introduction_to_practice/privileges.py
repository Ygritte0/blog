#-*-coding:utf-8-*-
from user2 import User
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