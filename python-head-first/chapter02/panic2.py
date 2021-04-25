phrase = "Don't panic!"
plist = list(phrase)
print(phrase) 
print(plist)


for i in range(4):
    plist.pop()

plist.pop(0)
plist.remove("'")

plist.extend([plist.pop(),plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

'''
this is the code presented on the python heads first
a little different from the one i created. in this case they are using
the plist.pop to remove and plist.extend to change the order of the charters
but still gave the same result.
'''