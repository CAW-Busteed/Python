def get_lcp(array):

    def comp_lcp(le, position, list):
        for word in list:
            if word[position] == le:
                continue
            else:
                return False
        return True

    result = []
    pos = 0
    for letter in array[0]:
        words = array[1:]
        if comp_lcp(letter, pos, words) == True:
            pos += 1
            result.append(letter)
        else:
            break
    return ''.join(result)
