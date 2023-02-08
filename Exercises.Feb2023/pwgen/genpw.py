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


SHORT = 'short'
MED = 'medium'
LONG = 'long'

let_ = list(string.ascii_letters)
sym_ = list(string.punctuation)
num_ = list(string.digits)
word_ = ['avocado', 'penguin', 'giraffe', 'brave', 'telephone', 'superfluous', 'hydrodynamic', 'zoo', 'moist', 'banana', 'corn', 'damsel', 'explode', 'french']

def ran_choice():
    arr = []
    for _set in (let_, sym_, num_):
      arr.append(random.choice(_set))
      choices = ''.join(arr)
    return choices       

def create_pw(_password, _len, _range):
        while len(_password) < random.randrange(_range[0], _range[1]):
            _password = _password + ran_choice()
            if len(_password) < _len:
                _password = _password + random.choice(word_)
            else:
                continue
        return _password

def pass_gen(n):
    password = ""

    if n == SHORT:
        while len(password) < 8:
            password = password + ran_choice()
        return password  
    
    elif n == MED:
        return create_pw(password, 4, (12, 17))

    elif n == LONG:
        return create_pw(password, 10, (20, 32))
 
    else:
        return 'Answer not applicable. Please choose SHORT, medium, or long.'
    
if __name__ == '__main__':
    LENGTH = input(f'Please clarify if you would like a {SHORT}, {MED}, or {LONG} password. ')
    print(pass_gen(LENGTH))
