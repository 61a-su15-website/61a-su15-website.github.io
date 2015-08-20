def list_demos():
    suits = ['coin', 'string', 'myriad']  # A list literal
    original_suits = suits
    suits.pop()             # Removes and returns the final element
    suits.remove('string')  # Removes the first element that equals the argument
    suits.append('cup')              # Add an element to the end
    suits.extend(['sword', 'club'])  # Add all elements of a list to the end
    suits[2] = 'spade'  # Replace an element
    suits
    suits[0:2] = ['heart', 'diamond']  # Replace a slice
    [suit.upper() for suit in suits]
    [suit[1:4] for suit in suits if len(suit) == 5]

def string_demo():
    string = "ABC"
    string[2] = 'e'
    len('apple')
    'banana'[:2]
    x, y = 1, 2
    '{} + {} = {}'.format(x, y, x + y)
    words = 'This is a sentence.'.split()
    words
    ' '.join(words)

def group_by_key(pairs):
    """
    Return a dictionary maps unique keys to corresponding values from
    a list of [key, value] pairs

    >>> example = [ [1, 2], [3, 2], [1, 3], [3, 1], [1, 2] ]
    >>> group_by_key(example)
    {1: [2, 3, 2], 3: [2, 1]}
    """
    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = [value]
        else:
            d[key].append(value)
    return d

def tuple_demos():
    (3, 4, 5, 6)
    3, 4, 5, 6
    ()
    tuple()
    tuple([1, 2, 3])
    # tuple(2)
    (2,)
    (3, 4) + (5, 6)
    (3, 4, 5) * 2
    5 in (3, 4, 5)
    {(1, 2): 3}
    # {([1], 2): 3}
    {tuple([1, 2]): 3}

def identity_demos():
    a = [10]
    b = a
    a == b
    a is b
    a.extend([20, 30])
    a == b
    a is b

    a = [10]
    b = [10]
    a == b
    a is not b
    a.append(20)
    a != b

# Mutable functions (bank accounts)

def make_withdraw(balance):
    """
    Return a withdraw function with a starting balance.
    >>> withdraw = make_withdraw(100)
    >>> withdraw(25)
    75
    >>> withdraw(25)
    50
    >>> withdraw(75)
    'Insufficient funds'
    >>> withdraw(50)
    0
    >>> new_withdraw = make_withdraw(10)
    >>> new_withdraw(5)
    5
    >>> withdraw(0)
    0
    """
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw
