'''
Objective:
    determine probabilty for an element in an array
    input would be the element
    output would be the probablity in percentage up to two decimal points
Procedure:
    count instances of element in list
    compare to length of list and calculate
    Bonus: catagorize based on rarity
'''



test_list = [1, 2, 3, 4, 5, 5, 6, 3, 3, 3, 3, 7, 8, 9, 10, 11, 11, 12, 11, 14, 15, 16, 20, 20, 21]

def probability_id(element_, list_):
    occur = list_.count(element_)
    return (occur / len(list_))*100

user_choice = input('Give an element to check: ')

result = probability_id(user_choice,test_list)

print(f'There is a' [result]'percent chance of this element appearing in the list.')

