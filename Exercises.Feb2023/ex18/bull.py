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


def compare(numbers, guess):
    cow = 0
    bull = 0
    for x in numbers:
        if x in guess:
            # if guess[x] == numbers[x]:
            #     cow+=1
            # else:
                bull+=1
        else:
            pass
    return bull


    # for x in range(len(numbers)):
    #     if numbers[x] == guess[x]:
    #         cow+=1
    #         #return cow
        


if __name__=="__main__":
    NUM_ = [random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)]
    tally = 0
    

    while True:
            #explanation and start of loop
            print('A return of a cow means a correct number and correct place. A bull is a correct guess in the wrong place.')
            trial = input('Guess a 4 digit number: ')

            #exit condition
            if trial == 'quit':
                break
            
            compare(NUM_, trial)
            pass


    

            



    
    


