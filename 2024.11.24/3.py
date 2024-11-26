def tree_leaves(branch_list: list) -> int:
    """Функция считает количество строк со значением 'leaf' в списке."""
    num = 0
    for branch in branch_list:
        if type(branch) is list:
            num += tree_leaves(branch)
        elif type(branch) is str:
            num += 1
    return num
    
tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]



# >>> tree_leaves(tree)
# 38