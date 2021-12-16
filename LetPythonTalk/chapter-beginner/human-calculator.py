from mysr import voice_to_text
from mysay import print_say

# Ask the lenght of the rectangle

print_say('What is the length of the rectangle')
inp1 = voice_to_text()
print_say(f'You just said {inp1}.')

# Ask the width of the rectanble
print_say('What is the width of the rectangle')
inp2 = voice_to_text()
print_say(f'You just said {inp2}')

# Calculate the area

area = float(inp1)*float(inp2)
# print and speak the result
print_say(f'The area of the rectangle is {area}.')
