import random

def tree_generator(level_recursion=0) -> list:
    """Функция генерирует и возвращает дерево элементов типа список. 
    Вложенные элементы могут быть строки ('leaf') или списки, 
    которые в свою очередь могут содержать как листья, так и строки. 
    Дерево не может быть пустым, но списки внутри дерева могут. 
    Функция принимает по умолчанию значение уровня вложенности рекурсии = 0."""
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