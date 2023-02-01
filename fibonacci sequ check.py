
num = int(input('How many numbers down the Fibonacci sequence do you want to check?  '))

#fibonacci function
def fibonacci(n):
    x, y = 1, 1
    fib_list = [x, y]
    for i in range(n-2):
        x1, y1 = x, y # prep to swap
        x = y1 #redefine x
        y = x1 + y1 #redefine new y val
        #add into list
        fib_list.append(y)
    return fib_list

print(fibonacci(num))







                




