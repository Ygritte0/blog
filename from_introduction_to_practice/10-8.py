#-*-coding:utf-8-*-
# filenames = []
def file_read(filename):
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        # print("Sorry,the file " + filename + " does not exist.")
        pass
    else:
        for line in lines:
            print(line.rstrip())


filenames = ['cat.txt','dog.txt','dragon.txt']
for filename in filenames:
    file_read(filename)