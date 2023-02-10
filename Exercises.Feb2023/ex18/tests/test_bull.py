from ex18.bull import compare

# def test_df():
#     assert add.add(1, 2) == 3


def test_compare_ok():
    a = [1, 2, 3, 4]
    b = [3, 3, 3, 3]
    assert compare(a, b) == ['cow']


def test_compare_fail():
    a = [1, 2, 3, 4]
    b = [3, 6, 8, 7]
    assert compare(a, b) == ['bull']
    b = [4, 5, 3, 7]
    assert compare(a, b) == ['bull', 'cow']
