# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 23:12:51 2017
Vowels Code
@author: mmaldonadoc
"""

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)            
