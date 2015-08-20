###############
# Linked List #
###############

class Link:
    """
    >>> s = Link('Got')
    >>> s.append('to')
    >>> s.extend(Link('them', Link('all')))
    >>> s.insert(2, 'catch')
    >>> s.first
    'Got'
    >>> s.rest.first
    'to'
    >>> s.rest.rest.first
    'catch'
    >>> s.rest.rest.rest.first
    'them'
    >>> s.rest.rest.rest.rest.first
    'all'
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    #######################
    # Insertion interface #
    #######################

    def append(self, value):
        "*** YOUR CODE HERE ***"
        if self.rest is Link.empty:
            self.rest = Link(value)
        else:
            self.rest.append(value)


    def extend(self, other):
        if other is Link.empty:
            return
        elif self.rest is Link.empty:
            self.rest = Link(other.first)
            self.rest.extend(other.rest)
        else:
            self.rest.extend(other)

    def insert(self, index, value):
        if index == 0:
            self.rest = Link(self.first, self.rest)
            self.first = value
        elif self.rest is Link.empty:
            raise IndexError
        else:
            self.rest.insert(index - 1, value)

    ######################
    # Sequence interface #
    ######################

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, index):
        if index == 0:
            return self.first
        elif self.rest is Link.empty:
            raise IndexError
        return self.rest[index - 1]


    ############################
    # Representation interface #
    ############################

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link(' + repr(self.first) + ')'
        else:
            return 'Link({0}, {1})'.format(repr(self.first), repr(self.rest))

    def __str__(self):
        elements = []
        while self is not Link.empty:
            elements.append(str(self.first))
            self = self.rest
        return '<' + ' '.join(elements) + '>'
