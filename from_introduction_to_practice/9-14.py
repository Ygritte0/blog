#-*-coding:utf-8-*-
from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1,self.sides)
        print(x)


square = Die(20)
square.roll_die()