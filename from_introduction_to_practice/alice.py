#-*-coding:utf-8-*-
filename = r'D:\编程书籍\python从入门到实践\《Python编程》源代码文件\chapter_10\alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + ' words.')