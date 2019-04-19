#-*-coding:utf-8-*-
# def make_pizza(*toppings):
#     print(toppings)
#
# make_pizza('pepperoni')
# make_pizza('mushroom','green_peppers','extra cheese')

def make_pizza(*toppings):
    print('Making a pizza with the following toppings:')
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushroom','green_peppers','extra cheese')