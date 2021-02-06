# Define a function make fn repeater which takes in a one-argument function
# f and an integer x. It should return another function which takes in one
# argument, another integer. This function returns the result of applying f to
# x this number of times.
# Make sure to use recursion in your solution.

def make_func_repeater(f , x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(y):
        if y == 1:
            return f(x)
        else:
            return f(repeat(y - 1))
    return repeat

# Below is the iterative version of is prime, which returns True if positive
# integer n is a prime number and False otherwise:
# def is_prime(n):
#     if n == 1:
#         return False
#     k = 2
#     while k < n:
#         if n % k == 0:
#             return False
#         k += 1
#         return True
# Implement the recursive is prime function. Do not use a while loop, use
# recursion. As a reminder, an integer is considered prime if it has exactly two
# unique factors: 1 and itself.

def is_prime(n):
    def prime_helper(k):
        if k == n:
            return True
        elif n % k == 0 or n == 1:
            return False
        else:
            return prime_helper(k + 1)
    return prime_helper(2)

# print(is_prime(7))
# print(is_prime(10))
# print(is_prime(1))
