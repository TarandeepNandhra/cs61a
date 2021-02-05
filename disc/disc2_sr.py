# Self-reference refers to a particular design of HOF,
# where a function eventually returns itself.

# A self-referencing function will not return
# a function call, but rather the function object itself.


# Write a function print delayed that delays printing its argument until the
# next function call. print delayed takes in an argument x and returns a
# new function delay print. When delay print is called, it prints out x and
# returns another delay print.

def print_delayed(x):
    """Return a new function. This new function, when called,
    will print out x and return another function with the same
    behavior.

    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi")
    5
    <function print_delayed> # a function is returned
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

# Write a function print_n that can take in an integer n and returns
# a repeatable print function that can print the next n parameters. After the
# nth parameter, it just prints ”done”.

def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    def inner_print(x):
        if n == 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print


if __name__ == "__main__":
    import doctest
    doctest.testmod()
