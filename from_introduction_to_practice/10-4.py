#-*-coding:utf-8-*-
filename = 'guest_book.txt'
print("Please enter 'q' at anytime to quit")
while True:
    user_name = input("Enter your name please:")
    if user_name == 'q':
        break
    else:
        with open(filename,'a') as file_object:
            file_object.write(user_name + '\n')