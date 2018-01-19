#!/usr/bin/python3
# password.py - An insecure password locker program

PASSWORDS = {'email': 'Cvfghjdl$%l',
             'blog': 'Fgh$#vBn',
             'luggage': '45678'}

import sys,pyperclip   
if len(sys.argv) < 2:
    print('Usage: password.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # First Command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('password for ' + account + ' copied to the clipboard')
else:
    print('There is no account named ' + account )
