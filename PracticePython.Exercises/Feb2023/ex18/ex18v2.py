'''
To get cows & bulls

bullscows <- [] 
generated_list <- [A,B,C,D]
inputed_value <- [a,b,c,d]

for each number(i,n) in generated_list:
    for each number(j,m) in inputed_value:
        if n == m:
            if i == j:
                add 'cow' to bullscows
                break
            add 'bull' to bullscows
            break
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
# To get cows & bulls:
def get_cowandbull(gen,input):
    c_and_b = []
    for x,i in gen:
        for y,j in input:
            if x == y:
                if i== j:
                    c_and_b.append('cow')
                    break
                c_and_b.append('bull')
                break
    return c_and_b
