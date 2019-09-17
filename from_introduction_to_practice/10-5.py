#-*-coding:utf-8-*-
"""关于编程的调查"""
filename = 'reason.txt'
print("Enter 'q' at anytime to quit.")
while True:
    reason = input("Why do you like programming?")
    if reason == 'q':
        break
    else:
        with open(filename,'a') as file_object:
            file_object.write(reason + '\n')