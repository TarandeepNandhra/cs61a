def min_abs_indices(s):
    """Indices of all elements in list s that have the smallest absolute value.

    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    # find min abs value
    min_abs = min(map(abs, s))

    return [i for i in range(len(s)) if abs(s[i]) == min_abs]

def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list s.

    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, 3, -2, -3, 2, -4])
    1
    """
    max = -100
    for i in range(len(s) - 1):
        if max < s[i] + s[i + 1]:
            max = s[i] + s[i + 1]
    return max

# def largest_adj_sum(s):
#     max([s[i] + s[i + 1] for i in range(len(s) - 1)])

# zip(s[:-1], s[1:]) tuples of all adjacent elements
# a + b for a,b in zip(s[:-1], s[1:])

# dictionary comprehension

def digit_dict(s):
    """Map each digit d to the lists of elements in s that end with d.

    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """

    return {d: [x for x in s if x % 10 == d] for d in range(10) if any([x % 10 == d for x in s])}

    # last_digits = [x % 10 for x in s] can break it up

def all_have_an_equal(s):
    """Does every element equal some other element in s?

    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    return not False in [s[i] in s[ : i] + s[i + 1 : ] for i in range(len(s))]

    # can also put an all in front of list comprehension instead of not False in.
