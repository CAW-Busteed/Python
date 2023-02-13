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
# NUM_ = [random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)]

#TODO find a way to put all these together more efficiently
num_w = str(random.randint(0,9))
num_x = str(random.randint(0,9))
num_y = str(random.randint(0,9))
num_z = str(random.randint(0,9))
NUM_ = [num_w, num_x, num_y, num_z]

# 'A return of a cow means a correct number and correct place. A bull is a correct guess in the wrong place. Guess 4-digits. '
# user_comp = input(str(start_mes))

# def num_check(n):
#     if ''.join(NUM_) == user_comp:
#             tally = tally + 1
#             return('All cows, correct!')
#             return(tally)
#     else:
#         response = []
#         sim = [x for x in [*user_comp] if x in NUM_]
#         if len(sim) > 0:


def compare(x, y):
    return 1
    

            



    
    


