import re

# Implement a generator function called filter(iterable, fn)
# that only yields elements of iterable for which fn returns True.
def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for i in iterable:
        if fn(i):
            yield i

# Tutorial: Write a generator function merge that takes in two infinite generators a
# and b that are in increasing order without duplicates and returns a generator that
# has all the elements of both generators, in increasing order, without duplicates

def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    x = next(a)
    y = next(b)
    while True:
        if x < y:
            yield x
            x = next(a)
        elif y < x:
            yield y
            y = next(b)
        else:
            yield x
            x , y = next(a), next(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
