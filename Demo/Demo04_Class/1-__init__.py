#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'FrozenSky'

# Define Class
class FighterPlane:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed
    def move(self):
        print('The %s is Flying...'%self.model)

# Create Class
F_15 = FighterPlane('F15', 450)

print('Model: %s'%F_15.model)
print('Speed: %s'%F_15.speed)
F_15.move()
