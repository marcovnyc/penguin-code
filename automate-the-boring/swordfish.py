while True:
    print('Who are you')
    name = input()
    if name != 'Legolas':
        continue
    print('Hello Legolas. What is your password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
    print('Access Granted' + name )
