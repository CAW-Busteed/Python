'''
missing<-[]
#walk through list
for number in sequence:
    #if gap
    for number in range from [current number] to [next number]
        if number+1 is not equal to [next number]
            #add missing numbers to list
            add [number+1] to missing list
    if the missing list is equal to the number of places requested, return [last number in missing list]
'''
def find_lastmissingno(arr, k) -> int:
    missingno = []
    for num in arr:
        for nmueral in range(num,):
            if nmueral+1 !=
            missingno.append(nmueral)
        if len(missingno) == k-1:
            break
    return missingno[k-1]