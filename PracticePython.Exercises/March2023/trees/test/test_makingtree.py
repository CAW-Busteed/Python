from trees.makingtree import Treenode
from trees.makingtree import identify_treelevel


def test_make_tree():
    root = Treenode("Arbora")
    root.add_child(Treenode("joe"))
    root.add_child(Treenode("cedric"))

    myresult = []
    root.print_tree(myresult)
    assert len(myresult) == 3
    assert myresult[0] == 'Arbora'
    assert myresult[1] == '   joe'
    assert myresult[-1] == '   cedric'

def test_identify_treelevel0():
    string = "The nature of the hologram is threefold:"
    assert identify_treelevel(string) == [0,string]

def test_identify_treelevel1():
    string = "   It is made of light."
    assert identify_treelevel(string) == [1,'It is made of light.']

def test_identify_treelevel2():
    string = "      It can be observed from any angle."
    assert identify_treelevel(string) == [2, 'It can be observed from any angle.']

def test_identify_treelevel3():
    string = "         And it can be programmed to achieve its form."
    assert identify_treelevel(string) == [3, "And it can be programmed to achieve its form."]
