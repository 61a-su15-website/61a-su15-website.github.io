def sum_digits(n):
    """
    Return the sum of the digits of positive integer n.

    >>> sum_digits(9)
    9
    >>> sum_digits(18117)
    18
    >>> sum_digits(9437184)
    36
    >>> sum_digits(11408855402054064613470328848384)
    126
    """
    if n < 10:
        return n
    else:
        rest, first = n // 10, n % 10
        return sum_digits(rest) + first

def is_prime(n):
    """
    Return whether n is a prime number

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(6)
    False
    >>> is_prime(11)
    True
    """
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
