######################
# Inheritance review #
######################

class Pokemon:
    def __init__(self):
        self.hp = 10

    def attack(self, other):
        if self.hp <= 0:
            return
        print(self.name, 'used', self.move)
        other.hp -= self.damage


class Pikachu(Pokemon):
    name = 'Pikachu'
    move = 'thunder'
    damage = 5


class Squirtle(Pokemon):
    name = 'Squirtle'
    move = 'water gun'
    damage = 3


class Zubat(Pokemon):
    name = 'Zubat'
    move = 'leech life'
    damage = 1

    def attack(self, other):
        Pokemon.attack(self, other)
        # The following line will execute even
        # if Zubat has no hp. For simplicity's
        # sake, we'll keep it like this.
        self.hp += self.damage


########################
# Mutable Linked Lists #
########################

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest


def map(lst, fn):
    """Mutatively applies fn on elements of lst.

    >>> s = Link(3, Link(2, Link(1)))
    >>> square = lambda x: x * x
    >>> map(s, square)
    >>> s.first            # square(3)
    9
    >>> s.rest.first       # square(2)
    4
    >>> s.rest.rest.first  # square(1)
    1
    """
    "*** YOUR CODE HERE ***"
    while lst != Link.empty:
        lst.first = fn(lst.first)
        lst = lst.rest


def insert_in_order(lst, e):
    if e < lst.first:
        lst.rest = Link(lst.first,
                        lst.rest)
        lst.first = e
    elif lst.rest is Link.empty:
        lst.rest = Link(e)
    else:
        insert_in_order(lst.rest, e)


def insertion_sort(lst):
    """Sorts the linked list using insertion sort.

    >>> s = Link(3, Link(2, Link(4, Link(1))))
    >>> insertion_sort(s)
    >>> s.first
    1
    >>> s.rest.first
    2
    >>> s.rest.rest.first
    3
    >>> s.rest.rest.rest.first
    4
    """
    unsorted = lst.rest
    sorted = lst
    sorted.rest = Link.empty
    while unsorted is not Link.empty:
        insert_in_order(sorted, unsorted.first)
        unsorted = unsorted.rest

