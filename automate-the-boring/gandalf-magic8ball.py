import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It Must Certainly Happen'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes Yes Yes!'
    elif answerNumber == 4:
        return 'My ball is not clear ask again!'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate Dear Friend and ask again'
    elif answerNumber == 7:
        return ' My Reply is NO!!'
    elif answerNumber == 8:
        return 'Outlook not so Good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
