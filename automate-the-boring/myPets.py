myPets = ['Rio', 'Peach', 'Francisco', 'Baby' ]
print('Enter a Pet Name')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name )
else:
    print(name + ' is my pet')
