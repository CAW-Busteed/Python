'''
To get cows & bulls

bullscows <- [] 
generated_list <- [A,B,C,D]
inputed_value <- [a,b,c,d]

for each number(i,n) in generated_list:
    for each number(j,m) in inputed_value:
        if position matches and item matches:
           we have a cow; break # handle next outer elem
        elif item matches:
           we have a bull; break # handle next outer elem
        else:
           do nothing; next elem # continue
return bullscows



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
    for x, i in gen:
        for y, j in input:
            #TODO: rectify flaw where repeating numbers can be counted as bulls rather than a single cow
            if x == y and i == j:
                c_and_b.append('cow')
                break
            elif i == j:
                c_and_b.append('bull')
                break
    return c_and_b

gen1 = enumerate([1,2,3,4])
input1 = enumerate([1, 2, 3, 5])
print(get_cowandbull(gen1,input1))

if __name__ == "__main__":
    generated_num = [
        random.int(0, 9),
        random.int(0, 9),
        random.int(0, 9),
        random.int(0, 9)
    ]

    print(
        'A cow means a correct placement and correct number. Bull just means a correct number'
    )
    answer = input()
    [int(x) for x in answer]
