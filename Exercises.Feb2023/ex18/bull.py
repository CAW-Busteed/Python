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

# TODO: rename i, j to a, b in all funcs

def get_cows(a,b):
    """
    this function computes the # of cows, returns a list..
    """
    cows = []
    for i, j in zip(a, b):
        if i == j:
            cows.append(i)   
    return cows

def get_not_cows(i,j):
    notcows = []
    for a,b in zip(i,j):
        if a != b:
            notcows.append([a, b])
    return notcows

def get_bulls(i, j):
    bulls = [x for x in i if x in j]
    return bulls
    
def cowbulls(a, b):
    cows_ = get_cows(a,b)
    pbulls_ = get_not_cows(a,b)

    # transpose a matrix
    pbulls1, pbulls2 = [], []
    for _a,_b in pbulls_:
        pbulls1.append(_a)
        pbulls2.append(_b)

    bulls_ = get_bulls(pbulls1, pbulls2)
    return [cows_, bulls_]

        

#main loop
if __name__=="__main__":
    # generate a random 4-digit num.
    num_ = [random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)]
    tally = 0 # tally is how many user attempts
    #run = True # flag to terminate main loop.

    #explanation and start of loop
    print('A return of a cow means a correct number and correct place. A bull is a correct guess in the wrong place.')
    while True:
            #user input
            ans_ = input('Guess a 4 digit number: ')

            #exit condition
            if ans_ == 'quit':
                break
            
            #transform input into list
            trial = [int(x) for x in ans_]

            # use cowbulls function to compare
            count_ = cowbulls(num_,trial)

            #add to tally
            tally+=1

            #tell user their score
            print(f'You have {len(count_[0])} cows and {len(count_[1])} bulls.')

            if len(count_[0]) == 4:
                print(f'All cows, you win! You guessed {tally} times')
                break
            else:
                print('Try again!')





    

            



    
    


