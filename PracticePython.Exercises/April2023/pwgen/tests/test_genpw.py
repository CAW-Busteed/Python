import genpw

def test_ran_choice():
    assert len(genpw.ran_choice()) == 3
    
def test_pwgen_short():
    x = len(genpw.pass_gen('short'))
    assert x <= 9 

def test_pwgen_med():
    x = len(genpw.pass_gen('medium'))
    assert (x >= 12 and x <= 18) 

def test_pwgen_long():
    x = len(genpw.pass_gen('long'))
    assert (x >= 20 and x <= 32)
