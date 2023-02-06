from pwgen import genpw

def test_pwgen_shor():
    x = len(genpw.pass_gen('short'))
    assert x <= 9 

def test_pwgen_med():
    x = len(genpw.pass_gen('medium'))
    assert (x >= 12 and x <= 18) 

def test_pwgen_long():
    x = len(genpw.pass_gen('long'))
    assert (x >= 20 and x <= 32)
