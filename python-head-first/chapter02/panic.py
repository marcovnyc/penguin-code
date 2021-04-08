#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 00:43:21 2021

@author: sofia
"""

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
combination = []
letters = ['o', 'n', ' ', 't', 'a', 'p']
print(letters)

new_combination = []
for letra in phrase:
    for letra in letters:
        if letra not in combination:
            combination.append(letra)
for letra in combination:
    new_combination.append(letra)
    print(new_combination)
            
            
        


new_phrase = ''.join(new_combination)
print(new_phrase)