print('Hello Aragorn, The orcs will be from 0 to 100 if you add all the orcs from 0 to 100 how many orcs will you fight?')
orcs = 0
for num in range(100):
    orcs = orcs + num
print('Aragorn you are in bad luck, you will fight ' + str(orcs) + ' orcs. Time to prepare')
