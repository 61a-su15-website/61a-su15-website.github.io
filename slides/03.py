# Review: Control structures

def sum_odds(n):
    """Returns the sum of all positive odd integers
    between 1 and n inclusive.

    >>> sum_odds(6)     # 1 + 3 + 5
    9
    >>> sum_odds(5)     # 1 + 3 + 5
    9
    """
    "*** YOUR CODE HERE ***"
    i, total = 1, 0
    while i <= n:
        if i % 2 == 1:
            total += i
        i += 1
    return total

# Generalization

def square(x):
    return x * x

def cube(x):
    return x * x * x

def sum_squares(n):
    i, total = 1, 0
    while i <= n:
        total += square(i)
        i += 1
    return total

def sum_cubes(n):
    i, total = 1, 0
    while i <= n:
        total += cube(i)
        i += 1
    return total

sum_squares(4)
sum_cubes(4)

# Functions as arguments

def summation(term, n):
    i, total = 1, 0
    while i <= n:
        total += term(i)
        i += 1
    return total

summation(square, 4)
summation(cube, 4)

# Sum the first n powers of two
def pow2(i):
    return pow(2, i)

summation(pow2, 4)

