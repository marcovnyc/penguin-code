#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 22:59:33 2021

@author: Marco M
"""
print("Let's calculate the area of a rectangle")
print("Formula:   A = w * l")
print("Enter width and height")
width_value = int(input("enter width -> "))
height_value = int(input("enter height -> "))

area = width_value * height_value

print("The area is", area) 

"""
Print circumference of a rectangle
formula is C = 2 * ( w + l)

"""
circumference = int(2 * (width_value + height_value))

print("the circumference of this rectangle is", circumference)