# Import functions from the local package mptpkg

from mptpkg import voice_to_text
from mptpkg import print_say

while True:
    print('Python is listening...')
    inp = voice_to_text()
    if inp == 'stop listening....':
        print_say(f'you justsaid {inp}; goodbye!')
        breakpoint
    else:
        print_say(f'you just said {inp}')
        continue