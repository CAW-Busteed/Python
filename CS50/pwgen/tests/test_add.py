from pwgen import add

votes = [
    ['Brad', 'Harold', 'Stacy'],
    ['Brad', 'Harold', 'Stacy'],
    ['Stacy', 'Brad', 'Harold'],
    ['Stacy', 'Brad', 'Harold'],
    ['Harold', 'Stacy', 'Brad'],
]


def test_tie():
    '''
    test that Brad and Harold are currently tied
    '''
