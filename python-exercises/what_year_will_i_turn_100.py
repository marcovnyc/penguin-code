#!/usr/bin/env python

import time



current_year = time.strftime("%Y") # Get current year
print("hello")
name = input("What is your name ")
age = input("What is your age ")
int_age = int(age)
int_current_year = int(current_year)
in_this_many_years = 100 - int_age
future_year =  int_current_year + in_this_many_years
str_future_year = str(future_year)
#print(future_year)
#print(in_this_many_years)
print("Hello " + name )

print("You will be 100 years old in the year " + str_future_year)
