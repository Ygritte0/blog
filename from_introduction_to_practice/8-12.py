#-*-coding:utf-8-*-
def make_sandwich(*toppings):
    print("I will add " + str(toppings) + " in your sandwich")
    for topping in toppings:
        print('- ' + topping)

make_sandwich('pepperoni','cheese','sausage')
