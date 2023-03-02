'''
input = a list of strings
pos <- 0 (initial psoition)
function get_LCP(input)
    for each letter(alpha) in the first word
        for each word in rest of input:
            IF alpha = word[pos]:
                do nothing
            ELSE:
                break
            pos+=1
    print pos
'''


def get_lcp(_input):
    pos = 0
    for c in _input[0]:
        for word in _input[1:]:
            if c == word[pos]:
                pass
            else:
                break
            pos += 1
    return _input[0][:pos]
