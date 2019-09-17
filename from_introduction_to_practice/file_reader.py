#-*-coding:utf-8-*-
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())
#     print("========")



file_path = r'D:\编程书籍\python从入门到实践\《Python编程》源代码文件\chapter_10\pi_digits.txt'
with open(file_path) as file_object:
    # # contents = file_object.read()
    # for line in file_object:
    # # print(contents.rstrip())
    #     print(line.rstrip())
    # print("---------------")
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())