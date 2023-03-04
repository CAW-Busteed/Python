from least_common_prefix.lcp import get_lcp

def test_get_lcp():
    strs = ['flower', 'flow', 'flair']
    assert get_lcp(strs) == 'fl'

def test_fail_get_lcp():
    strs = ['vorpal', 'vanquish', 'vain']
    assert get_lcp(strs) == 'v'

def test_fail_2_get_lcp():
    strs = ['cat', 'dog', 'vain']
    assert get_lcp(strs) == ''