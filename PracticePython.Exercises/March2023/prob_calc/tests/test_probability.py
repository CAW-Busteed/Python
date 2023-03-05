from prob_calc import probability

def test_probability_id():
    a = [1, 2, 3, 4, 5, 5, 6, 3, 3, 3]
    assert probability_id(3, a) == 0.4
    