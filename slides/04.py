# Functions as arguments (from lecture 3)

def summation(term, n):
    i, total = 1, 0
    while i <= n:
        total += term(i)
        i += 1
    return total

# Local function definitions; returning functions

def make_adder(n):
    """Return func that takes one arg k and returns k + n

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

    return lambda k: k + n

# Practice with HOFs

summation(lambda x: x**2, 3)

def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3

result = repeat(g, 5)
