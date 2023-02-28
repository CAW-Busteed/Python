from dictionary_ex import pull_rans

def test_pull_rans():
    sample_text = "bana"
    message = "banana"
    assert pull_rans(sample_text, message) == False