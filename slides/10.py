# Floating point representation

(103/191)*191


# Rational arithmetic

def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """Multiply rational numbers x and y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def eq_rational(x, y):
    """Return whether rational numbers x and y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Print rational x."""
    print(numer(x), "/", denom(x))


# Constructor and selectors

def rational(n, d):
    """Construct a rational number x that represents n/d."""
    return [n, d]

def numer(x):
    """Return the numerator of rational number x."""
    return x[0]

def denom(x):
    """Return the denominator of rational number x."""
    return x[1]


# Improved constructor

from fractions import gcd
def rational(n, d):
    """Construct a rational that represents n/d in lowest terms."""
    g = gcd(n, d)
    return [n//g, d//g]


# Functional implementation

def rational(n, d):
    """Construct a functional representation of n/d."""
    g = gcd(n, d)
    n, d = n//g, d//g
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select

def numer(x):
    """Return the numerator of functional rational number x."""
    return x('n')

def denom(x):
    """Return the denominator of functional rational number x."""
    return x('d')


# Mobiles

def total_weight(m):
    """Return the weight of a mobile

    >>> m = mobile(branch(1, obj(2)), branch(2, obj(1)))
    >>> total_weight(m)
    3
    """
    if is_obj(m):
        return weight(m)
    else:
        lc, rc = contents(left(m)), contents(right(m))
        return total_weight(lc) + total_weight(rc)

# Abstraction Violations!
def total_weight_abs_violation(m):
    if m[0] == 'object':
        return m[1]
    else:
        lc, rc = m[1][1], m[2][1]
        return total_weight(lc) + total_weight(rc)

def is_balanced(m):
    """Return whether the mobile is balanced

    >>> m = mobile(branch(1, obj(2)), branch(2, obj(1)))
    >>> is_balanced(m)
    True
    >>> m = mobile(branch(1, obj(2)), branch(1, obj(1)))
    >>> is_balanced(m)
    False
    """
    if is_obj(m):
        return True
    else:
        torque_eq = torque(left(m)) == torque(right(m))
        lc, rc = contents(left(m)), contents(right(m))
        return torque_eq and is_balanced(lc) and is_balanced(rc)

# Mobile ADT

def mobile(left, right):
    """Construct a mobile from left and right branches"""
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile"""
    return m[0] == 'mobile'

def left(mobile):
    """Return the left branch of a mobile"""
    return mobile[1]

def right(mobile):
    """Return the right branch of a mobile"""
    return mobile[2]

# Branch ADT

def branch(length, contents):
    """Construct a branch; contains an object or a mobile"""
    return [length, contents]

def length(branch):
    """Return the length of a branch"""
    return branch[0]

def contents(branch):
    """Return the contents of a branch"""
    return branch[1]

def torque(b):
    """Return the torque on a branch"""
    return length(b) * total_weight(contents(b))

# Object ADT

def obj(weight):
    """Construct a weighted object"""
    return ['object', weight]

def is_obj(o):
    """Return whether o is an object"""
    return o[0] == 'object'

def weight(o):
    """Return the weight of an object"""
    return o[1]
