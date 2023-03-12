'''
To get cows & bulls

gen <- [A,B,C,D]
input <- [a,b,c,d]

reduced_gen = []  # holding array for computing bulls
reduced_input = []  # holding array#2 for computing bulls

flags = [] # for computing bulls
c_and_b = []  # result array

# compute cows; get reduced array for computing bulls
for index and value in enumerated gen
    if value = input[index]:
        add 'cow' to c_and_b
    else: 
        #add values to reduced_gen and reduced_input
        add value to reduced_gen
        add input[index] to reduced_input
        
# compute bulls from reduced array
create a flag1 array as long as length of reduced_input
for x in gen):
    for i, y in enumerate(reduced_input):
        if x=y and flag[i] = True:
            add 'bull' to c_and_b
            flag[i] = false

introduce main loop
    generate a random 4 digit number
    game loop begins
        request input from user
        compare input to generation and ID no. of cows and bulls
        if no. of cows is 4, 
            signal victory and break
            otherwise loop restarts
'''
import random


# To get cows & bulls:
def get_cowandbull(gen, input):
    c_and_b = []  # result array
    reduced_gen = []  # holding array for computing bulls
    reduced_input = []  # holding array#2 for computing bulls
    flags = []

    # first we compute cows (because cows > bulls)
    for i, x in enumerate(gen):
        if x == input[i]:
            c_and_b.append('cow')
        else:
            reduced_gen.append(x)
            reduced_input.append(input[i])

    # create a boolean array to mark elements in input that have already been considered
    for x in reduced_input:
        flags.append(True)

    # for identical value in reduced_gen and reduced_input:
    for x in reduced_gen:
        for i, y in enumerate(reduced_input):
            if x == y and flags[i] == True:
                c_and_b.append('bull')
                flags[i] = False

    return c_and_b


# if __name__ == "__main__":
#     generated_num = [
#         random.int(0, 9),
#         random.int(0, 9),
#         random.int(0, 9),
#         random.int(0, 9)
#     ]

#     print(
#         'A cow means a correct placement and correct number. Bull just means a correct number'
#     )
#     answer = input()
#     [int(x) for x in answer]
