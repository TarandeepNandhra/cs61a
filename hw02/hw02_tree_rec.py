def next_largest_coin(coin):
    """Return the next coin.
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

    def check_count(total, coins, index):
        if total == 0:
            return 1
        elif total < 0 or len(coins) == index:
            return 0
        else:
            return check_count(total - coins[index], coins, index) + check_count(total, coins, index + 1)
    return check_count(total, [1, 5, 10, 25], 0)

# Uses next coin rather than an array for coins.

def count_coins(total):
    def count_coins_helper(total, largest):
        if total == 0:
            return 1
        elif total < 0 or largest == None:
            return 0
        else:
            return count_coins_helper(total - largest, largest) + count_coins_helper(total, next_largest_coin(largest))
    return count_coins_helper(total, 1)

print(count_coins(100))
