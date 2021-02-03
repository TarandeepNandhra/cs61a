def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    total = n
    counter = 1
    while counter < k:
        n -= 1
        counter += 1
        total *= n
    return total

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    #recusive version - refactored
    if y == 0:
        return y
    else:
        y_rest, y_last = y // 10, y % 10
        return y_last + sum_digits(y_rest)

'''
 s = str(y)
    total = 0
    for i in range(len(s)):
        total += int(s[i])
    return total
'''

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    #false neg if input is 0 - could add an assert or seperate case
    def eights_helper(n, prev):
        if n == 0:
            return False
        if n % 10 == prev:
            return True
        else:
            return eights_helper(n // 10 , n % 10)
    return eights_helper(n // 10, n % 10)

'''
    s = str(n)
    for i in range(len(s)):
        if int(s[i]) == 8 and int(s[i + 1]) == 8:
            return True
    return False
print(double_eights(8000088))
'''
