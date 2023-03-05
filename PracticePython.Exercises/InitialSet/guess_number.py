'''
def compare

generate ANSWER
tally = 0 
while true:
    collect input (as int)
    compare to ANSWER:
    if value == -1
        print too low
        tally +1
    if value == +1
        print too high
        tally +1
    if value == 0
        print congrats
        print tally total
        break

'''


import random
NUM = random.randint(1,9)
tally = 0

def compare(NUM, GUESS):
    if NUM > GUESS:
        return -1
    elif NUM < GUESS:
        return +1
    else:
        return 0


while True:
    GUESS = int(input('I am thinking of a number between 1 and 9. Care to guess? '))
    if GUESS == 'exit':
        break
    else:
        result = compare(NUM, GUESS)
        if result == -1:
            tally = tally+1
            print('Too low, try again!')
        elif NUM < GUESS:
            tally = tally+1
            print('Too high, try again!')
        elif NUM == GUESS:
            print('Correct, you win!')
            tally = tally+1
            print(f"You tried {tally} times.")
            break
        else:
            print('Please use a number between 1 and 9')