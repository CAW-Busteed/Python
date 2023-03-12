from ex18_v2.bull import get_cowandbull


def test_get_allcows():
    a = [1, 2, 3, 4]
    b = [1, 2, 3, 4]
    assert get_cowandbull(a, b) == ['cow', 'cow', 'cow', 'cow']


def test_get_some_cows():
    a = [1, 2, 2, 4]
    b = [1, 2, 3, 4]
    assert get_cowandbull(a, b) == ['cow', 'cow', 'cow']


def test_get_some_cows_arrays_exchanged():
    a = [1, 2, 2, 4]
    b = [1, 2, 3, 4]
    assert get_cowandbull(b, a) == ['cow', 'cow', 'cow']


def test_get_cowandbull_with_dup_cows():
    a = [2, 2, 2, 2]
    b = [1, 2, 3, 4]
    assert get_cowandbull(a, b) == ['cow']


def test_get_allbulls():
    a = [4, 3, 2, 1]
    b = [1, 2, 3, 4]
    assert get_cowandbull(a, b) == ['bull', 'bull', 'bull', 'bull']


def test_get_nomatches():
    a = [4, 3, 2, 1]
    b = [8, 7, 6, 5]
    assert get_cowandbull(a, b) == []
