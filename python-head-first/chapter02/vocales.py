#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 22:05:08 2021

@author: sofia
"""

vocales = ['a', 'e', 'i', 'o', 'u']
palabra = "superfragilisticoexperadiliosus"
for letra in palabra:
    if letra in vocales:
        print(letra)