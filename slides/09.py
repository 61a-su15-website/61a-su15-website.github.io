def sum(lst):
    """Add all the numbers in lst. Use iteration.

    >>> sum([1, 3, 3, 7])
    14
    >>> sum([])
    0
    """
    "*** YOUR CODE HERE ***"
    total = 0
    for elem in lst:
        total += elem
    return total

def count(d, v):
    """Return the number of times v occurs as
    a value in dictionary d.

    >>> d = {'a': 4, 'b': 3, 'c': 4}
    >>> count(d, 4)
    2
    >>> count(d, 3)
    1
    >>> count(d, 1)
    0
    """
    "*** YOUR CODE HERE ***"
    total = 0
    for val in d.values():
        if val == v:
            total += 1
    return total


def most_frequent(lst):
    """Return the element in lst that occurs
    the most number of times.

    >>> lst = [1, 4, 2, 4]
    >>> most_frequent(lst)
    4
    """
    "*** YOUR CODE HERE ***"
    count = {}
    for elem in lst:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1
    return max(count, key=lambda k: count[k])
