from pwgen import ranked_voting

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
    choice= []
    for x in votes:
        # for y in x:
        #     choice.append(y)
        # for y in choice: