'''
missing <- []
for idx, num in enumerated(arr[1:]):
  a, b = num, next-num
  if (b-a)>1:   
    # gap exists in pair
    add a+1 .. b-1 to missing    
'''


def find_lastmissingno(arr, k) -> int:
    missingno = []
    for idx, num in enumerate(arr[1:]):
        a, b = arr[idx], arr[idx + 1]
        if (b - a) > 1:
            for i in range(a + 1, b):
                missingno.append(i)
    print(missingno)


arr = [1, 2, 3, 5, 6, 9, 10, 11, 13, 17]
k = 3
find_lastmissingno(arr, k)
