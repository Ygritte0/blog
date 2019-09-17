#-*-coding:utf-8-*-
print("Give me two numbers, I'll add them for you.")
print("Enter 'q' to quit.")
while True:
    try:
        first_number = input('first number:')
        if first_number == 'q':
            break
        x = int(first_number)
        second_number = input('second number:')
        if second_number == 'q':
            break
        y = int(second_number)
    except ValueError:
        msg = "Numbers are expected!"
        print(msg)
    else:
        answer = x + y
        print(str(answer))