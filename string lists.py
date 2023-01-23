#input sample
word = input('Write a word: ')
#turn into string
word = str(word)
#identify ::-1 as backwards, considering 0 is first string
reverse = word[::-1]
print(reverse)
if word == reverse:
    print('This word is a palindrome')
else:
    print('It is not a palindrome')