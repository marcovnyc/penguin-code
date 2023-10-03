import random
answers = ['not today', 'come back later', 'don\'t count on it', 'most likely', 'maybe', 'for sure']
random_answer = random.choice(answers)

question = input('What is your question! ')
# print(random_answer)


print('  ##  ')
print('The Magic 8 Ball Says!')
print(question)
print(random_answer)
print('You must listen and do as I say')

