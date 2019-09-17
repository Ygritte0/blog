#-*-coding:utf-8-*-
# import json
# def greet_user():
#     """问候用户并指出其名字"""
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("What's your name? ")
#         with open(filename,'w') as f_obj:
#             json.dump(username,f_obj)
#             print("We'll remember you when you come back, " + username + '!')
#     else:
#         print("Welcome to back, " + username + '!')

import json
def get__stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(filename,f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get__stored_username()
    if username:
        correct = input("Are you " + username + '? (y/n)')
        if correct == 'y':
            print("Welcome back " + username + "!")
        else:
            username = get_new_username()
            print("I'll remember you when you come back " + username + '!')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + '!')

greet_user()