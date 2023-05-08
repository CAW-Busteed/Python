from fizzbuzz.fizzbuzzfinder import find_fizzbuzz
def test_fizzbuzz15():
    assert find_fizzbuzz(16) == [ 'fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz']

def test_findfizzbuzz30():
    assert find_fizzbuzz(31) == [ 'fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz', 'fizz', 'buzz', 'fizz', 'fizz', 'buzz', 'fizz', 'fizzbuzz']