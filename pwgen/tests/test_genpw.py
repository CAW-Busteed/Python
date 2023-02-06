from pwgen import genpw

def test_pwgen():
    assert genpw.ran_choice(1) == 'abc'

