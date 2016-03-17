__author__ = 'mushahidalam'


def word_count(string):
    i = 0
    n = len(string)
    temp = ''
    word_dict = dict()
    for i in range(n):
        if string[i] != ' ':
            temp += string[i]
        else:
            if temp in word_dict:
                word_dict[temp] += 1
            else:
                word_dict[temp] = 1
            temp = ''
        if i == n - 1:
            if temp in word_dict:
                word_dict[temp] += 1
            else:
                word_dict[temp] = 1
            temp = ''
    print(word_dict)


string = 'hi this hi this not'
word_count(string)
