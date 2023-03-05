from dictionary_ex import pull_rans

def test_pull_rans():
    MAGAZINE = "bana"
    RANSOM = "banana"
    assert pull_rans(MAGAZINE,RANSOM) == False

def test_take_rans():
    MAGAZINE = "banana"
    RANSOM = "banna"
    assert pull_rans(MAGAZINE, RANSOM) == True
