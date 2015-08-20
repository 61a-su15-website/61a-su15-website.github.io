def fib(n):
    """Compute the nth Fibonacci number."""
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

def can_win(n):
    """Returns True if we can guarantee a win by starting at n cookies. Each
    player can take either 1 cookie or 2 cookies at a time.

    >>> can_win(0)
    False
    >>> can_win(1)
    True
    >>> can_win(2)
    True
    >>> can_win(3)
    False
    >>> can_win(4)
    True
    >>> can_win(9)
    False
    >>> can_win(10)
    True
    """
    if n == 0:
        return False
    elif n == 1:
        return True
    take_one = not can_win(n - 1)
    take_two = not can_win(n - 2)
    return take_one or take_two

def count_partitions(n, m):
    """Counts the number of ways to partition the integer n using non-negative
    integers less than or equal to m.

    >>> count_partitions(6, 4)
    9
    >>> count_partitions(4, 1)
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0
    else:
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return with_m + without_m
