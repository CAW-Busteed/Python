# a = [1, 1, 3, 4, 4, 5, 6, 7, 7, 8, 12, 15, 17, 19, 22, 24, 27, 29, 50]
# b = [4, 6, 8, 12, 22, 27, 28, 29, 35, 66, 90]
# res = [x for x in a if x in b]
# print(res)


# Objective: get first and last num in list, inside a function

a = [5, 10, 15, 20, 25]

def find_range(list):
    minimum = list[0]
    maximum = list[-1]
    return [minimum, maximum]
    #return [minimum] +' is the smallest in the list, and '+ maximum + ' is the biggest.'



print(find_range(a))
