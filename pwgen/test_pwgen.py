import pwgen

def test_pwgen():
    assert pwgen.ran_choice(1) == 'abc'

