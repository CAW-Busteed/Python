

def pull_rans(magazine, ransom):
    mdict = {}
    for e in magazine:
        if e not in mdict:
            mdict[e] = 1
        else:
            mdict[e] = mdict[e] + 1
            
    for e in ransom:
        if e not in mdict:
            return False
        else:
            mdict[e]-=1
            if mdict[e] < 0:
                return False
            
            
    return True

    # mdict[e] = mdict[e] + 1
    # mdict['h'] = mdict[e] + 1

sample_text = "bana"
message = "banana"

print(pull_rans(sample_text, message))
