ans = [1, 2, 5, 7]
guess = [1, 2, 4, 5]

# for x in zip(ans, guess):
#     print(f'{x[0] == x[1]}')


def cowbulls(i, j):
    def cows_id(i,j):
        cows = []
        for x in zip(i, j):
            if x[0] == x[1]:
                cows.append(x[0])   
        return cows

    def not_cows(i,j):
        notcows = []
        for x in zip(i,j):
            if x[0] == x[1]:
                continue
            else:
                notcows.append([x[0], x[1]])
        return notcows

    def bulls_id(i, j):
        bulls = [x for x in i if x in j]
        return bulls
    
    cows_ = cows_id(i,j)
    pbulls_ = not_cows(i,j)
    pbulls1, pbulls2 = [], []
    for a,b in pbulls_:
        pbulls1.append(a)
        pbulls2.append(b)
    bulls_ = bulls_id(pbulls1, pbulls2)
    return [cows_, bulls_]


print(cowbulls(ans, guess))


# arr = [[1, 2], [3, 4], [5, 6]]
# l1, l2 = [], []

# for a,b  in arr:
#     l1.append(a)
#     l2.append(b)







