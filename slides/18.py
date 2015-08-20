######################
# Linked List Review #
######################

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' +helper(link).rstrip() +'>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' +helper(link.first).rstrip() + '> '+ helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

def link_extend(s1, s2):
    """
    Mutatively extend s1 with s2

    >>> s1 = Link(1)
    >>> s2 = Link(2)
    >>> link_extend(s1, s2)
    >>> s2.rest = Link(3)
    >>> print_link(s1)
    <1 2>
    """
    if s2 is Link.empty:
        return
    elif s1.rest is Link.empty:
        s1.rest = Link(s2.first)
        link_extend(s1.rest, s2.rest)
    else:
        link_extend(s1.rest, s2)

def link_extend(s1, s2):
    """
    Mutatively extend s1 with s2

    >>> s1 = Link(1)
    >>> s2 = Link(2)
    >>> link_extend(s1, s2)
    >>> s2.rest = Link(3)
    >>> print_link(s1)
    <1 2>
    """
    while s1.rest is not Link.empty:
        s1 = s1.rest
    while s2 is not Link.empty:
        s1.rest = Link(s2.first)
        s1 = s1.rest
        s2 = s2.rest

##############
# Tree Class #
##############

class Tree:
    def __init__(self, entry, subtrees=[]):
        for s in subtrees:
            assert isinstance(s, Tree), 'each subtree must be a Tree'
        self.entry = entry
        self.subtrees = list(subtrees)

    def is_leaf(self):
        return not self.subtrees

def tree_contains(t, e):
    """
    Return if the Tree t contains the value e

    >>> t = Tree(1, [
    ...         Tree(4, [Tree(2), Tree(3, [Tree(1)])]),
    ...         Tree(5),
    ...         Tree(8, [Tree(6)])])
    >>> tree_contains(t, 8)
    True
    >>> tree_contains(t, 7)
    False
    """
    return e == t.entry or \
            any([tree_contains(s, e) for s in t.subtrees])

def tree_map(t, fn):
    """
    Mutates every entry in the Tree t by applying function fn
    """
    t.entry = fn(t.entry)
    for s in t.subtrees:
        tree_map(s, fn)

############################
# Binary Search Tree Class #
############################
class BinaryTree:
    empty = ()

    def __init__(self, entry, left=empty, right=empty):
        self.entry = entry
        self.left = left
        self.right = right

def bst_contains(t, s):
    """
    Return if BST t contains value s
    """
    if e == t.entry:
        return True
    elif e < t.entry:
        return bst_contains(t.left, e)
    else:
        return bst_contains(t.right, e)
