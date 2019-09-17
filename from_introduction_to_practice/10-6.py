#-*-coding:utf-8-*-
print("Give me two numbers, I'll add them for you.")
# print("Enter 'q' to quit.")
try:
    first_number = input('first number:')
    x = int(first_number)
    second_number = input('second number:')
    y = int(second_number)


except ValueError:
    msg = "Numbers are expected!"
    print(msg)

else:
    answer = x + y
    print(str(answer))