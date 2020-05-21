"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

# Practice 9.2.1
def longer_than_20(word):
    return 20 < len(myWord):

# Practice 9.2.2
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

# Practice 9.2.3
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

# Practice 9.2.4
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

# Practice 9.2.5
def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True
    
if __name__ == '__main__':
    fin = open('.\\assets\\words.txt')
    print_len20(fin)
    fin.close()