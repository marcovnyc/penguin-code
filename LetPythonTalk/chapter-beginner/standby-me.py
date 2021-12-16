from mysr import voice_to_text

while True:
    print('Python is listening...')
    inp = voice_to_text()
    print('you just said {input}' .format(input=inp))
    if inp == 'stop listening':
        print('Goodbye')
        break