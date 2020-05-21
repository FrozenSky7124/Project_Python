"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

def times_of_double(word):
    i = 0
    time = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            time = time + 1
            i = i + 2
        else:
            i = i + 1
    return time
    
if __name__ == '__main__':
    fin = open('.\\assets\\words.txt')
    for line in fin:
        myword = fin.readline().strip()
        if times_of_double(myword) >= 3:
            print(myword)
    fin.close()