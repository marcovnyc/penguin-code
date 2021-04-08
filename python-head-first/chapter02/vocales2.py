#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 22:05:08 2021

@author: sofia
"""

vocales = ['a', 'e', 'i', 'o', 'u']
palabra = input("Escribe una oracion aqui: ")
encontradas = []
for letra in palabra:
    if letra in vocales:
        if letra not in encontradas:
            encontradas.append(letra)
for letra in encontradas:
    print(letra)