#-*-coding:utf-8-*-
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []
    # 让每一个magician变成magician the great,并加入great_magicians
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' '+ 'the Great'
        great_magicians.append(great_magician)
    # 此时，magicians 的列表已经是空列表了，把加完the great的“great magicians”再次加到magicians 列表里
    return great_magicians
    # for great_magician in great_magicians:
    #     magicians.append(great_magician)
    #
    # return magicians

magicians = ['Alice', 'July', 'Kevin','Lily','Sansa','John']
print(id(magicians))
#
# show_magicians(magicians)
make_great(magicians[:])
show_magicians(make_great(magicians[:]))
show_magicians(magicians)
# print('============')
# show_magicians(magicians)