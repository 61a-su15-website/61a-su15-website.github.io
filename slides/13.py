######################
# Linked List review #
######################

def insert(lst, item, index):
    """Returns a link matching lst but with the given item
    inserted at the specified index. If the index is
    greater than the current length, the item is appended
    to the end of the list.

    >>> lst = link(1, link(2, link(3)))
    >>> new = insert(lst, 42, 2)
    >>> print_link(new)
    1 2 42 3
    """
    "*** YOUR CODE HERE ***"
    if index == 0 or lst == empty:
        return link(item, lst)
    else:
        return link(first(lst), insert(rest(lst), item, index - 1))

# Linked list ADT

empty = []

def link(first, rest=empty):
    return [first, rest]

def first(s):
    return s[0]

def rest(s):
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)


#########
# Trees #
#########

def sum_tree(t):
    """Sums up all entries in a tree.

    >>> t = tree(4,
    ...          [tree(3),
    ...           tree(2,
    ...                [tree(5)]),
    ...           tree(1)])
    >>> sum_tree(t)   # 4 + 3 + 2 + 5 + 1
    15
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return entry(t)
    total = entry(t)
    for subtree in subtrees(t):
        total += sum_tree(subtree)
    return total

def map_tree(t, fn):
    """Returns a new tree with fn applied on all entries
    in a tree.

    >>> t = tree(4,
    ...          [tree(3),
    ...           tree(2,
    ...                [tree(5)]),
    ...           tree(1)])
    >>> new = map_tree(t, lambda x: x * x)
    >>> print_tree(new)
    16
        9
        4
            25
        1
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(fn(entry(t)))
    lst = []
    for subtree in subtrees(t):
        lst = lst + [map_tree(subtree, fn)]
    return tree(fn(entry(t)), lst)

# Tree ADT

def tree(entry, subtrees=[]):
    return [entry] + list(subtrees)

def entry(t):
    return t[0]

def subtrees(t):
    return t[1:]

def is_leaf(t):
    return not subtrees(t)

def print_tree(t, indent=0):
    print('    ' * indent + repr(entry(t)))
    for s in subtrees(t):
        print_tree(s, indent + 1)

