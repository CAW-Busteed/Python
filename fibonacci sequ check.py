'''
Objective: rturn list containing fibonacci sequence up 
to user's input number. Reminder that fibon sequence =
1+1=2+1=3+2=5+3=8+5=13...

Define function where x+y over and over
if len(num) then break

'''
# #initial fibonacci list
fib_list = [1, 1]

# #quik add function
# def add_val(x, y):
#     return x + y


# num = int(input(print('How many numbers down the Fibonacci sequence do you want to check?' )))

#fibonacci function
def fibonacci(n):
    x, y = 1, 1
    # for i in range(n):
    #     x, y = y, (x+y)
    #     print(y)

    if n == 1:
        return str('You "one"! Hahaha...But seriously its just one')
    elif n == 2:
        return str('"Two" bad! Bahaha...I crack myself up. The list so far is just') + [fib_list]
    else:
        fib_list.append(x+y)
        print(fib_list)
        x = x+y
        if len(fib_list) == n:
            return fib_list
    
        else:
            fib_list.append(x+y)
            print(fib_list)
            y = (x+y)
            if len(fib_list) == n-1:
                return fib_list
            else:
                fib_list.append(x+y)
                print(fib_list)
                x = x+y
                if len(fib_list) == n:
                    return fib_list
                else:
                    fib_list.append(x+y)
                    print(fib_list)
                    y = (x+y)
                    if len(fib_list) == n:
                        return fib_list


print(fibonacci(12))







                




