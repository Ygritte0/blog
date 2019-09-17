#-*-coding:utf-8-*-
def word_the_count(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print("The file " + filename + ' does not exist.')
    else:
        word_the = contents.lower().count('the')
        # num_the = len(word_the)
        print("The file " + filename + " has about " + str(word_the) + "'the's." )


filenames = ['little_women.txt','alice.txt','Gone with wind']
for filename in filenames:
    word_the_count(filename)