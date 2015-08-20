def is_prime(n):
    """Returns True if n is a prime number, False otherwise.

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(15)
    False
    >>> is_prime(97)
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

