from ex18.bull import compare
from ex18.bull import cowbulls


# def test_df():
#     assert add.add(1, 2) == 3

def test_cowbulls():
    a = [1, 2, 3, 4]
    b = [4, 2, 3, 3]
    assert cowbulls(a,b) == [[2, 3], [4]]

# def test_bulls_id():
#     a = [1, 4, 3, 2]
#     b = [3, 2, 3, 3]
#     assert bulls_id(a,b) == [3, 2]
#     b = [2, 8, 7, 9]
#     assert bulls_id(a,b) == [2]

# def test_cows_id():
#     a = [1, 2, 3, 4]
#     b = [3, 2, 3, 3]
#     assert cows_id(a,b) == [2, 3]


# def test_compare_ok():
#     a = [1, 2, 3, 4]
#     b = [3, 2, 3, 3]
#     assert compare(a,b) == [1, 1]
#     #TODO: Correct answer would be [0, 2]
#     a = [1, 3, 4, 4]
#     b = [3, 3, 3, 3]
#     assert compare(a,b) == [1, 0]
#     #TODO: Correct answer would be [1, 0]
#     a = [1, 2, 3, 4]
#     b = [3, 2, 4, 3]
#     assert compare(a,b) == [2, 1]
#     a = [1, 2, 3, 4]
#     b = [5, 6, 7, 8]
#     assert compare(a,b) == [0, 0]
    

# def test_compare_fail():
#     a = [1, 2, 3, 4]
#     b = [3, 6, 8, 7]
#     assert compare(a,b) == [1, 0]
#     b = [4, 5, 3, 7]
#     assert compare(a,b) == [1, 1]