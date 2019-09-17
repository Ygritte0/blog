#-*-coding:utf-8-*-
import json
def get_stored_number():
    """如果存储了用户喜欢的数字，就显示它"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            number_loved = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number_loved

def get_new_number():
    """提示用户输入新的数字"""
    number_loved = input("What's your favorite number? ")
    filename = "favorite_number.json"
    with open(filename) as f_obj:
        json.dump(number_loved,f_obj)
        return number_loved

def favorite_number():
    """说出用户喜欢的数字"""
    number_loved = get_stored_number()
    if number_loved:
        print("I know your favorite number. It's " + number_loved)
    else:
        number_loved = get_new_number()
        filename = 'favorite_number.json'
        with open(filename,'w') as f_obj:
            json.dump(number_loved,f_obj)
            print("I know your favorite number! It's " + number)

favorite_number()