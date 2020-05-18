"""
This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

def right_justify(s):
    strLen = len(s)
    print(' ' * (70 - strLen) + s)
	
right_justify('monty')