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


# def compare(numbers, guess):
#     cow = 0
#     bull = 0
#     for (i,x) in enumerate(numbers):
#         for (j,y) in enumerate(guess):
#             if i == j and x == y:
#                 cow+=1
#                 break
#             elif x == y:
#                 bull+=1
#                 break
#             else:
#                 continue
#         else:
#             continue
#     return [bull, cow]


def cowbulls(i, j):
    def cows_id(i,j):
        cows = []
        for x in zip(i, j):
            if x[0] == x[1]:
                cows.append(x[0])   
        return cows

    def not_cows(i,j):
        notcows = []
        for x in zip(i,j):
            if x[0] == x[1]:
                continue
            else:
                notcows.append([x[0], x[1]])
        return notcows

    def bulls_id(i, j):
        bulls = [x for x in i if x in j]
        return bulls
    
    cows_ = cows_id(i,j)
    pbulls_ = not_cows(i,j)
    pbulls1, pbulls2 = [], []
    for a,b in pbulls_:
        pbulls1.append(a)
        pbulls2.append(b)
    bulls_ = bulls_id(pbulls1, pbulls2)
    return [[cows_], [bulls_]]



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
            
            # compare(NUM_, trial)
            pass


    

            



    
    

