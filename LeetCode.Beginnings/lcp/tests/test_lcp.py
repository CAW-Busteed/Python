from lcp import get_lcp

def test_get_lcp():
    strs = ['flower', 'flow', 'flair']
    assert get_lcp(strs) == 'fl'