'''fizzbuzz<- [] #strings denoting factors of three(’fizz’), factors of five (‘buzz’), and factors of fifteen (‘fizzbuzz’)

For a number in a set range (1-100):
	If the number is divisible by 15, add ‘fizzbuzz’ to fizzbuzz
	else:
If the number is divisible by 3, add ‘fizz’ to fizzbuzz
		If the number is divisible by 5, add ‘buzz’ to fizzbuzz'''



def find_fizzbuzz(upto):
    #result strings denoting factors of three(’fizz’), factors of five (‘buzz’), 
    # and factors of fifteen (‘fizzbuzz’)
    fizzbuzz = []

    for num in range(1,upto):
        if num % 15 == 0:
            #If the number is divisible by 15, add ‘fizzbuzz’ to fizzbuzz
            fizzbuzz.append('fizzbuzz')
        #since 15 is divisble by both 5 and 3, it had to be done first
        elif num % 3 == 0:
            fizzbuzz.append('fizz')
        elif num % 5 == 0:
            fizzbuzz.append('buzz')
    return fizzbuzz
