from kth_number.missing_num import find_lastmissingno


def test_find_lastmissingno():
    arr = [1, 2, 3, 5, 6, 9, 10, 11, 13, 17]
    k = 3
    assert find_lastmissingno(arr, k) == 12
