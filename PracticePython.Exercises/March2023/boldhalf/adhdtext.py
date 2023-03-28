'''There is a way of bolding text to make it easier for people with ADHD to read.
Input string
seperate string by word into list
find the midpoint of every word
    divide length of word by 2, place 
bold the first half using html
rejoin words as a string
'''

get_string = "This is a sample sentence. Note the first half of every word is encapuslated by a bold effect."

def bold_half(string):
    product = []
    list = string.split()
    for word in list:
        midpoint = (len(word)//2)
        if midpoint < 1:
            midpoint = 1
        bolding = '[b]' + word[:midpoint] + '[/b]' + word[midpoint:]
        product.append(bolding)
    return ' '.join(product)

print(bold_half(get_string))

