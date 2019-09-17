#-*-coding:utf-8-*-
user_name = input("Please tell me your name:")
filename  = 'guest.txt'
with open(filename,'a') as file_object:
    file_object.write(user_name+'\n')