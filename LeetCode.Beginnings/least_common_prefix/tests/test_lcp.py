from least_common_prefix.lcp import get_lcp

def test_get_lcp():
    strs = ['flower', 'flow', 'flair']
    assert get_lcp(strs) == 'fl'

def fail_test_get_lcp():
    strs = ['vorpal', 'vanquish', 'vain']
    assert get_lcp(strs) == 'v'

def fail_test2_get_lcp():
    strs = ['cat', 'dog', 'vain']
    assert get_lcp(strs) == ''