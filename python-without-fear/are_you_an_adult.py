age = int(input('Enter your age, please: '))
name_str = str(input('Enter your name please: '))
print('Happy Day ',  name_str,  '.', sep='')
print('Your are', age, 'years old')
if age > 12 and age < 20:
    print('Your are a teenager')
else:
    print('You are an adult')
