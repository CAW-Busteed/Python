'''
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) 
and another number. 
The function decides whether or not the given number is inside the list and returns
 (then prints)
an appropriate boolean.
'''

arr = [1, 3, 5, 30, 42, 43, 45, 50, 74, 98, 100, 500]

#replicate array to manipulate
check_arr = arr


def parse(guess, list):
    for x in list:
        if x == guess:
            print(f'{guess} is in the list.')
            break
    else:
        print(f'{guess} is not in the list.')



#input the number to check list
guess_ = int(input('Choose a number to check: '))

while True:
    #set up divider to binary search from
    indx = int((len(check_arr))/2)

    #match index point to guess
    if check_arr[indx] == guess_:
        print(f'{guess_} is in the list')
        break

    #fail condition, should there be only one left in list, or the guess is larger or smaller than the  biggest and smallest elements repectively
    # could also replace     elif indx == 0     with    elif len(check_arr) == 1
    elif indx == 0 or guess_ < check_arr[0] or guess_ > check_arr[-1]:
        print(f'{guess_} is not in the list')
        break
    
    #if the index point is too big, delete it and all larger numbers from temp array
    elif check_arr[indx] > guess_:
        del check_arr[indx:len(check_arr)]

    #if the index point is too small, delete all numbers leading up to it from temp array
    elif check_arr[indx] < guess_:
        del check_arr[:indx]
    

    
    
