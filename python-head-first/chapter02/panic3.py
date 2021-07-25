trance = "don't panic!"
word = list(trance)

new_phrase = ''.join(word[1:3])
new_phrase = new_phrase + ''.join([word[5],word[4],word[7],word[6]])

print(word)
print(new_phrase)