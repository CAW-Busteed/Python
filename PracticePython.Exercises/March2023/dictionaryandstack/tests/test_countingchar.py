from dictionaryandstack.countingchar import charactercount

def test_charactercount():
    a = ['cat', 'dog']
    assert charactercount(a) == {"c":1, "a":1, "t":1, "d":1, "o":1, "g":1}

def test_multicharactercount():
    a = ['cat', 'dog', 'avoca']
    assert charactercount(a) == {"c":2, "a":3, "t":1, "d":1, "o":2, "g":1, "v":1}

def test_nocharactercount():
    a = []
    assert charactercount(a) == {}