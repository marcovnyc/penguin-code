import time
import sys

# Import functions for make python talk package mptpkg
from mptpkg import voice_to_text
from mptpkg import print_say

# Print and announce the rules for the game in a human voice
print_say(''' Thinks of an integer,
         bigger or equal to 1 but smaller than equal to 9''')
print("Is it 5?")

while True:
    re1 = voice_to_text()
    print_say(f"You just said {re1}")
    if re1 in ("too high", "that is right", "to small"):
        break
    if re1 == "that is right":
        print_say("Yay Lucky Me")
        sys.exit
    