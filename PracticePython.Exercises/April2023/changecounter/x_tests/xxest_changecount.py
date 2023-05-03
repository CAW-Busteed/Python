from change_counter import coin_count

def test_coincount1():
    assert coin_count(25) == 1

def test_coincount2():
    assert coin_count(31) == 3

def test_coincount3():
    assert coin_count(99) == 9

