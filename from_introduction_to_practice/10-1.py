#-*-coding:utf-8-*-
filename = 'D:\编程书籍\python从入门到实践\《Python编程》源代码文件\chapter_10\learning_python.txt'
# filename.replace('python','C')
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.replace('Python','C'))

print("==============")
with open(filename) as file_object:
    for line in file_object:

        print(line.replace('Python','C').rstrip())

print("++++++++++++++++")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python','ruby').rstrip())

