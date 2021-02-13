this_file = __file__

# Write a function which takes in an integer a and returns a one-argument function.
# This function should take in some value b and return a + b the first time it is called, similar to make_adder.
# The second time it is called, however, it should return a + b + 1, then a + b + 2 the third time, and so on.
def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    def adder(x): # x is var to be incremented  a is amount of increment
        nonlocal a
        b = x + a
        a += 1  #each time a is incremented : after each call func increments another 1
        return b
    return adder

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    now, n, k = 0 , 0, 1
    def fib():
        nonlocal now, n, k
        now = n
        n , k = k , n + k
        return now
    return fib

# Write a function which takes in a list lst, an argument entry, and another argument elem.
# This function will check through each item present in lst to see if it is equivalent with entry.
# Upon finding an equivalent entry, the function should modify the list by placing elem into the list right after the found entry.
# At the end of the function, the modified list should be returned. See the doctests for examples on how this function is utilized.
# Use list mutation to modify the original list, no new lists should be created or returned.

def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    """
    "*** YOUR CODE HERE ***"
    nonlocal lst
    for i in range(lst):
        final.append(i)
        if i == entry:
            final.append(elem)
    lst = final
    return final
