# Simple program to name your cats
catNames = []
while True:
    print('Enter the name of your cat ' + str(len(catNames) + 1) + '(Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # Example of list concatenation
print('Cat Names are:')
for name in catNames:
    print('   ' + name)
