# years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
# ages = [2014 - year for year in years_of_birth]
# print(ages)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# evens = [ int % 2 == 0 for int in a]
#this ends up with a series of true and flases I want numbers
evens = [int for int in a if int % 2 == 0 ]
thriples = [int for int in a if int % 3 == 0]
print(evens)
print(thriples)