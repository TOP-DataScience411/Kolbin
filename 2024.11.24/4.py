import random

def tree_generator(level_recursion=0) -> list:
    tree = []
    branch_size = random.randrange(4)
    for i in range(branch_size):
        type_obj = random.randrange(2)
        if type_obj:
            tree.append("leaf")
        else:
            tree_local = tree_generator(level_recursion+1)
            tree.append(tree_local)
    if not level_recursion and not len(tree):
        tree = tree_generator()
    return tree
        


# >>> tree_generator()
# [[], 'leaf']
# >>> tree_generator()
# [['leaf'], ['leaf'], [[['leaf', 'leaf', 'leaf'], 'leaf', 'leaf'], 'leaf', ['leaf', ['leaf', ['leaf', 'leaf'], ['leaf', ['leaf']]], []]]]
# >>> tree_generator()
# ['leaf']