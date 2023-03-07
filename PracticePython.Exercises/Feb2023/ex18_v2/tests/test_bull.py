from ex18.bull import get_cows_and_bulls


def test_get_cowandbull():
    a = [1, 2, 3, 4]
    b = [3, 2, 3, 3]
    assert get_cows_and_bulls(a, b) == ([2, 3], [[1, 4], [3, 3]])
