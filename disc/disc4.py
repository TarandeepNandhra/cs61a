# You want to go up a flight of stairs that has n steps. You can either take 1
# or 2 steps each time. How many different ways can you go up this flight of stairs?
# Write a function count_stair_ways that solves this problem. Assume n is positive.

def count_stair_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

'''
a = count_stair_ways(3)
print(a)
'''

# Tutorial: Consider a special version of the count_stairways problem,
# where instead of taking 1 or 2 steps, we are able to take up to and including
# k steps at a time.
# Write a function count_k that figures out the number of paths for this scenario.
# Assume n and k are positive.


def count_k(n, k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        i = 1
        total = 0
        while i <= k:
            total += count_k(n - i, k)
            i += 1
    return total
'''
a = count_k(10, 3)
print(a)
'''

# Tutorial: Write a function that takes a list s and returns a new list
# that keeps only the even-indexed elements of s and multiplies them by their
# corresponding index.

def even_weighted(s):
    final = []
    for i in range(0, len(s) - 1):
        if i % 2 == 0:
            final += [int(s[i]) * i] # have to put [ ] to add in
    return final
'''
a = [1, 2, 3, 4, 5, 6]
print(even_weighted(a))
'''

# Write a function that takes in a list and returns the maximum product that
# can be formed using nonconsecutive elements of the list. The input list will
# contain only numbers greater than or equal to 1.

def max_product(s):
    if s == []:
        return 1
    if len(s) == 1:
        return s[0]
    else:
        return max( s[0] * max_product(s[2:]) , max_product(s[1:]))

a = [5,10,5,10,5]
print(max_product(a))
