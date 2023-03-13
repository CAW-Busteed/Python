'''count instances of letters in strings of words
chars<-empty dictionary
for every word in a list, split into letters
for every letter:
    if the letter is already in the dictionary, add one to its value
    otherwise, add it to the dictionary with a value of one
return dictionary'''

def charactercount(string):
    #chars<-empty dictionary
    chars = {}

    #for every word in a list, split into letters
    for word in string:
        for letter in list(word):
            # if the letter is already in the dictionary, add one to its value
            if letter in chars:
                chars[letter] = chars[letter]+1
            else:
                chars.update({letter:1})
    return chars
