HW_SOURCE_FILE = __file__

def split(n):
    return n // 10, n % 10

def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    x_wo_last , last = split(x)

    if x_wo_last == 0 and last == 0:
        return 0
    elif last == 8:
        return num_eights(x_wo_last) + 1
    else:
        return num_eights(x_wo_last)

#a = num_eights(8000000)
#print(a)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # index 'i', ppn pingpong value and dir is 1 or - 1
    def helper(index, ppn, dir):
        if index == n:
            return ppn
        if num_eights(index) > 0 or index % 8 == 0:
            return helper(index + 1, ppn - dir, -dir)
        else:
            return helper(index + 1, ppn + dir, dir)
    return helper(1, 1, 1)

"""
Wrong type of implementation - instrucive
    def swaps(n):
        if 1 <= n <= 7:
            return 0
        if num_eights(n) > 0 or n % 8 == 0:
            return swaps(n - 1) + 1
        else:
            return swaps(n - 1)

    if 1 <= n <= 7:
        return n
    if swaps(n) % 2 == 0:
        return pingpong(n - 1) + 1
    else: # odd
        return pingpong(n - 1) - 1
"""

"""
Iterative version
def iter_pingpong(n):
    count = 1
    i = 1
    w = 0 # w = 1 - w
    while i < n:
        if num_eights(i) > 0 or i % 8 == 0:
            w = 1 - w
        if w == 0:
            count += 1
        if w == 1:
            count -= 1
        i += 1
    return count

#a = iter_pingpong(1)
#print(a)
"""

def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    n_but_last , last1 = split(n)
    last2 = split(n_but_last)[1]

    if n_but_last == 0: # single digit number
        return 0
    if last1 == last2: # repeated digit
        return missing_digits(n_but_last)

    return missing_digits(n_but_last) + last1 - last2 -1

# print(missing_digits(19))
