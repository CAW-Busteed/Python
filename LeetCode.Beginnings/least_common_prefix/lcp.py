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

# def get_lcp(_input):
#     pos =0
#     for c in _input[0]:
#         for word in _input[1:]:
#             if c == word[pos]:
#                 pass
#             else:
#                 break
#             pos+=1
#     return _input[0][:pos]



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
            pos+=1
            result.append(letter)
        else:
            break
    return ''.join(result)

example = ['repeat', 'reheat', 'repeal']
print(get_lcp(example))





    
