# for item in range(20):
#     if item == 6: break
#     print(item)
# else:
#     print('done!')

# list1 = [2]
# num = int(input('Check number: '))
# for x in list1:
#     if num % x == 0:
#         print('This is not a prime')
#         break
#     elif num == x:
#         print(list1, 'are the primes leading up to this one.')
#         break
#     else:
#         y = x+1
#         list1.append(y)
#         continue

def isOdd(x):
    return x % 2 == 1

li2 = list(range(1,25))
li3 = list(filter(isOdd, range(30, 200)))
li4 = li2 + li3
li5 = li2*2

print(li3)