number = int(input("Enter a number : "))
divisor =  int(input("What to divide by: "))
if number % 4 == 0:
    print("divisible by 4")
elif number % 2 == 0:
    print(number, "is even!")
else:
    print(number, "is odd!")

if number % divisor == 0:
    print(number, "divides evenly by", divisor)
else:
    print(number, "does not divide evenly by", divisor)