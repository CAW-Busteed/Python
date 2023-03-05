'''
Cows and Bulls

Randomly generate a 4-digit number. 
Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. 
Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

generated (n) is array of digits
'''
import random


def get_cows(actual, guess):
    """
    this function computes the # of cows, returns actual list of cows
    and actual reduced version (with cows removed) of the input arrays
    """
    return None


def get_bulls(actual, guess):
    "find matching bulls"
    return None


def get_cows_and_bulls(actual, guess):
    return None


#main loop
if __name__ == "__main__":
    # generate a random 4-digit num.
    num_ = [
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 9)
    ]

    tally = 0  # tally is how many user attempts
    #run = True # flag to terminate main loop.

    #explanation and start of loop
    print(
        'A return of a cow means a correct number and correct place. A bull is a correct guess in the wrong place.'
    )
    # while True:
    #     #user input
    #     ans_ = input('Guess a 4 digit number: ')
    # return None
