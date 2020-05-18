"""
This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)

def circle(t, r, n):
    c = 2 * 3.1415926 * r
    l = c / n
    polygon(t, l, n)

def arc(t, r, n, angle):
    c = 2 * 3.1415926 * r
    l = c / n
    for i in range(angle):
        t.fd(l)
        t.lt(360 / n)
    
bob = turtle.Turtle()

# square(bob, 200)
#polygon(bob, 100, 7)
#circle(bob, 200, 256)
arc(bob, 128, 360, 90)

turtle.mainloop()