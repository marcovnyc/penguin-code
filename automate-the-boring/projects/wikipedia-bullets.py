#!/usr/bin/python3

import pyperclip
text = pyperclip.paste()

 # Separate lines and add start

lines = text.split('\n')
for i in range(len(lines)): # Loop through all indexes in the "line" list
    lines[i] = '* ' + lines[i] # Add a start at the beginning of the line
text = '\n'.join(lines)
pyperclip.copy(text)
