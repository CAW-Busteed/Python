
num = int(input('How many numbers down the Fibonacci sequence do you want to check?  '))

#fibonacci function
def fibonacci(n):
    x, y = 1, 1
    fib_list = [x, y]
    for i in range(n-2):
        x, y = y, (x+y) #swap
        fib_list.append(y)
    return fib_list

print(fibonacci(num))







                




