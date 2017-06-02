# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:19:28 2017
The Elephant Song.
@author: marco
"""
word = "elefantes"

for num_elephants in range(0, 15, +1):
    print(num_elephants, word, "se columpiaban sobre")
    print("la tela de una arana y como vieron que resistia")
    print("Fueron a llamara otro elefante")
    if num_elephants == 15:
        print(num_elephants, "se columpiaban y la tela se rompio")
    else:
        swing_elephant = num_elephants + 1
        if swing_elephant == 1:
            word = "elefante"
        print(swing_elephant, word, "se columpiaba")
    print()