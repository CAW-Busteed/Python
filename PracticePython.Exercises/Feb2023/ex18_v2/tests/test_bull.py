from ex18_v2.bull import get_cowandbull


def test_get_cowandbull():
    a = enumerate([1, 2, 3, 4])
    b = enumerate([1, 2, 3, 5])
    assert get_cowandbull(a, b) == ['cow', 'cow', 'cow']

def test_get_cowandbull2():
    a = enumerate([1,2,2,4])
    b = enumerate([1,2,3,4])
    assert get_cowandbull(a, b) == ['cow', 'cow', 'cow']