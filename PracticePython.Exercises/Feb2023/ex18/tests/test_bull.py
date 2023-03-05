from ex18.bull import get_cows_and_bulls
from ex18.bull import get_bulls
from ex18.bull import get_cows


def test_get_cows():
    a = [1, 2, 3, 4]
    b = [3, 2, 3, 3]
    assert get_cows(a, b) == ([2, 3], [[1, 4], [3, 3]])


def test_get_bulls():
    a = [1, 4, 3, 2]
    b = [3, 2, 3, 3]
    assert get_bulls(a, b) == [3, 2]
    b = [2, 8, 7, 9]
    assert get_bulls(a, b) == [2]


def test_cows_and_bulls():
    a = [1, 2, 3, 4]
    b = [4, 2, 3, 3]
    assert get_cows_and_bulls(a, b) == [[2, 3], [4]]
