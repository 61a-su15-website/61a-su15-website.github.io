def get_item(lst, i):
    """Gets the element in the linked list
    at index i.

    >>> lst = link(1, link(2, link(3)))
    >>> get_item(lst, 0)
    1
    >>> get_item(lst, 2)
    3
    """
    "*** YOUR CODE HERE ***"
    while lst != empty:
        if i == 0:
            return first(lst)
        lst = rest(lst)
    return None

def append(lst, e):
    """Adds the element e to the end of lst.

    >>> lst = link(1, link(2, link(3)))
    >>> new = append(lst, 4)
    >>> first(rest(rest(rest(new))))
    4
    """
    "*** YOUR CODE HERE ***"
    if lst == empty:
        return link(e)
    new = append(rest(lst), e)
    return link(first(lst), new)

# Recursive
def reverse(lst):
    """Reverses the elements in lst."""
    "*** YOUR CODE HERE ***"
    if lst == empty:
        return empty
    new_rest = reverse(rest(lst))
    return append(new_rest, first(lst))

# Iterative
def reverse(lst):
    new = empty
    while lst != empty:
        new = link(first(lst), new)
        lst = rest(lst)
    return new

###################
# Linked list ADT #
###################

# Implemented as lists

empty = []

def link(first, rest=empty):
    return [first, rest]

def first(s):
    return s[0]

def rest(s):
    return s[1]

# Implemented as dispatch functions

empty = None

def link(first, rest=empty):
    def dispatch(msg):
        if msg == 'first':
            return first
        elif msg == 'rest':
            return rest
    return dispatch

def first(s):
    return s('first')

def rest(s):
    return s('rest')
