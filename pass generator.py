'''
random password generator
import random
generate lists of numbers, symbols, letters, and words
ask user to choose between easy, medium, and hard passwords
    easy length = 8, 1[word] 1-2[symbol] 1-4 [letters] and 1-4 [numbers]
    medium length = 12-17, 2[word] 3-4[symbol] 5-10[letters] and 5-10[numbers]
    hard length = 20-32, 4[word] 5-6[symbol] 11-18[letters] and 11-18[numbers]
randomize set length  in med and hard
randomize which lsit to pull from for every letter
    until len() is > x and <y
    return result


'''
import random
import string


let_ = list(string.ascii_letters)
sym_ = list(string.punctuation)
num_ = list(string.digits)
word_ = ['avocado', 'penguin', 'giraffe', 'brave', 'telephone', 'superfluous', 'hydrodynamic']

#user inputs password preference
LENGTH = input('Please clarify if you would like a short, medium, or long password. ')

def pass_gen(n):
    password = ""
    def ran_choice(n):
        x1 = random.choice(let_)
        x2 = random.choice(sym_)
        x3 = random.choice(num_)
        choices = x1 + x2 + x3
        return choices       
        
    if n == 'short':
        while len(password) < 8:
            password = password + ran_choice(n)
        return password  

    elif n == 'medium':
        while len(password) < random.randrange(12,17):
            password = password + ran_choice(n)
            #password = password + random.choice(word_)
        return password

    elif n == 'long':
        while len(password) < random.randrange(20,32):
            password = password + ran_choice(n)
            #password = password + random.choice(word_)
        return password
    else:
        return 'Answer not applicable. Please choose short, medium, or long.'
    

print(pass_gen(LENGTH))