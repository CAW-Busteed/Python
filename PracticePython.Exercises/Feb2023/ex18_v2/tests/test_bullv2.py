from ex18v2 import get_cowandbull


def test_get_cowandbull():
    a = [1, 2, 3, 4]
    b = [3, 2, 3, 3]
    assert get_cowandbull(a,b) ==  ([2, 3], [[1, 4], [3, 3]])