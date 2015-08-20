import time

def timeit(func, repeats=1):
    """
    Return a wrapper that times the execution of a function
    """
    def timed(*args, **kargs):
        """
        Print the execution time of the function
        """
        i = 0
        time0 = time.time()
        while i < repeats:
            result = func(*args, **kargs)
            i += 1
        time1 = time.time()
        print('Execution time:', time1 - time0)
        return result
    return timed

def factorial(n):
    """Return n!

    >>> factorial(0)
    1
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

timed_factorial = timeit(factorial, 1000)

def fib_rec(n):
    """Return the nth Fibonacci number

    >>> fib_rec(0)
    0
    >>> fib_rec(1)
    1
    >>> fib_rec(5)
    5
    """
    if n == 0 or n == 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

timed_fib_rec = timeit(fib_rec)

def fib_iter(n):
    """Return the nth Fibonacci number

    >>> fib_iter(0)
    0
    >>> fib_iter(1)
    1
    >>> fib_iter(5)
    5
    """
    cur, next = 0, 1
    while n > 0:
        cur, next = next, cur + next
        n -= 1
    return cur

timed_fib_iter = timeit(fib_iter)

def square(x):
    """Return x squared

    >>> square(2)
    4
    >>> square(3)
    9
    """
    return x * x

def pow_naive(b, n):
    """Return b ** n

    >>> pow_naive(2, 2)
    4
    >>> pow_naive(4, 5)
    1024
    """
    if n == 0:
        return 1
    else:
        return b * pow_naive(b, n - 1)

timed_pow_naive = timeit(pow_naive, 1000)

def pow_fast(b, n):
    """Return b ** n

    >>> pow_fast(2, 2)
    4
    >>> pow_fast(4, 5)
    1024
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(pow_fast(b, n // 2))
    else:
        return b * pow_fast(b, n - 1)

timed_pow_fast = timeit(pow_fast, 1000)

