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


def get_lcp_v2(words):
    """
    flag = 'unknown' # test if loop breaks
    count = 0        # character pos of current iteration

    for each triplet in words:
      if len(set(triplet)) != 1:
        flag = False
        break
      else:
        count += 1

    # loop is done; check flag and make decision
    if flag == 'unknown':
      flag = True

    """

    pos = 0
    for pos in range(len(words[0])):
        triplet = [word[pos] for word in words]
        if len(set(triplet)) != 1:
            break
    return words[0][:pos]
