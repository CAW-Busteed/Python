'''
To get cows & bulls

bullscows <- [] 
gen <- [A,B,C,D]
input <- [a,b,c,d]
gen2 <-[]
input2 <-[]
input_flag <- [true,true,true,true]


for index and value in enumerated gen
    if value = input[index]:
        add 'cow' to bullscows
    else: 
        #add values to gen2 and input2
        add value to gen2
        add input[index] to input2
        
for identical value in gen2 and input2
for x in gen2 and input2:
    add 'bull' to bullscows

Or...
create a flag1 array as long as length of input2
for x in gen):
    for i, y in enumerate(input2):
        if x=y and flag[i] = True:
            add 'bull' to bullscows
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
    c_and_b = []
    reduced_gen = []
    reduced_input = []
    flag =[]

    # for index and value in gen
    for i, x in enumerate(gen):
            #if value = input[index]:
            if x == input[i]:

                #add 'cow' to bullscows
                c_and_b.append('cow')

                # add value of gen to reduced_gen
                # add value of input to reduced_input
            else:
                reduced_gen.append(x)
                reduced_input.append(input[i])

    #create a flag1 array as long as length of input2 for x in gen):
    for x in reduced_input:
        flag.append(True)
  
    # for identical value in copy_gen and copy_input:
    for x in reduced_gen:

        # for i, y in enumerate(input2):
        for i,y in enumerate(reduced_input):

            #if x=y and flag[i] = True:
            if x==y and flag[i]==True:
                #add 'bull' to bullscows
                c_and_b.append('bull')
                flag[i]=False
   
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
