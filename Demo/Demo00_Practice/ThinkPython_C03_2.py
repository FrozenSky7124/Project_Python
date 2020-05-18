"""
This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

def print_twice(bruce):
    print(bruce)     
    print(bruce)

def do_twice(func, value):
    func(value)
    func(value)
    
do_twice(print_twice, 'spam')

def do_four(func, value):
    do_twice(func, value)
    do_twice(func, value)
    
do_four(print, 'spam')