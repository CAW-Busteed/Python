class Treenode:
    #these functions set up how to make a tree
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    #for proper ordering of print function
    def get_level(self):
        level = 0
        p = self.parent
        #for every level we go down, we count an ancestor in level
        while p:
            level += 1
            p = p.parent
        return level

    # And if I want to print it, it can be done recursively to return all leaves
    def print_tree(self, result=[]):
        prefix = ' ' * self.get_level(
        ) * 3  #can multiply number of spaces to make it more indented
        result.append(prefix + self.data)
        # print(prefix + self.data)
        if self.children:  #if len(self.children) > 0:
            for child in self.children:
                child.print_tree(result)


def build_mythos_tree():
    root = Treenode("Arbora")

    telves = Treenode("True Elves")
    telves.add_child(Treenode('High Elves'))
    telves.add_child(Treenode('Lesser Elves'))
    telves.add_child(Treenode('Terran Elves'))

    kidu = Treenode("Kidu")
    kidu.add_child(telves)

    nai = Treenode("Nai")
    nai.add_child(Treenode("Dryads"))

    glish = Treenode("Glish")
    glish.add_child(Treenode("Dwarves"))

    dohremi = Treenode('Dohremi')
    dohremi.add_child(Treenode('Fathume'))
    dohremi.add_child(Treenode('Sorreleta'))
    dohremi.add_child(Treenode('Lalrek'))
    dohremi.add_child(Treenode('Tipenum'))
    dohremi.add_child(Treenode('Fashal'))
    dohremi.add_child(Treenode('Solmm'))
    dohremi.add_child(Treenode('Lafey'))
    dohremi.add_child(Treenode('Tikeep'))
    dohremi.add_child(Treenode('Famoki'))
    dohremi.add_child(Treenode('Soushek'))
    dohremi.add_child(Treenode('Larach'))
    dohremi.add_child(Treenode('Ti'))

    jick = Treenode('Jick')
    jick.add_child(dohremi)

    ord = Treenode('Ord')
    ord.add_child(Treenode('Titans'))
    ord.add_child(Treenode('Goliaths'))

    fen = Treenode('Fen')
    fen.add_child(Treenode('Fairies'))
    fen.add_child(Treenode('Argites'))

    skorm = Treenode('Skorm')
    skorm.add_child(Treenode('Billipedes'))
    skorm.add_child(Treenode('Glak'))
    skorm.add_child(Treenode('Gluk'))
    skorm.add_child(Treenode('Orcum'))

    root.add_child(kidu)
    root.add_child(nai)
    root.add_child(glish)
    root.add_child(jick)
    root.add_child(ord)
    root.add_child(fen)
    root.add_child(skorm)

    return root


if "__main__" == __name__:
    root = build_mythos_tree()
    myresult = []
    root.print_tree(myresult)

    # print("\n".join(myresult))
    for elem in myresult:
        print(elem)
