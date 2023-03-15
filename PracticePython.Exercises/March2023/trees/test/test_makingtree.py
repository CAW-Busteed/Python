from trees.makingtree import Treenode


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
