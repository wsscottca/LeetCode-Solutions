'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:
    
Understand and Cases:
    coins = [1,2,3,5] amount = 5
    coins = [1,2,4,5,10] amount = 20

Design and Verify:
    Initial thought - sort coins then work backwards O(nlogn)
    O(N) - DP
    subproblem - # of coins to get to n
                 # of coins to get to n - curr coin
                 repeating
                 
          0  1  2  3  4  5  6  7  8  9 10 11 12
    dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3]
    coin = 5
    i = 5
    
    # treat the index as the amount
    # have it store the lowest number of coins to get to i
    dp = [(amount + 1) for _ in range(amount + 1)]
    dp[0] = 0
    
    # for each coin, update the fastest routes
    # past that coin
    for coin in coins:
        for i in range(coin, amount + 1):
            # is the previous route or current route less coins
            dp[i] = min(dp[i], dp[i-coin] + 1)
    
    # if we did not find a round to our amount with the given coins
    # return -1
    if dp[-1] > amount:
        return -1
    
    # otherwise return the least amount of coins to get to dp[-1]/dp[amount]
    return dp[-1]
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # treat the index as the amount
        # have it store the lowest number of coins to get to i
        dp = [(amount + 1) for _ in range(amount + 1)]
        dp[0] = 0

        # for each coin, update the fastest routes
        # past that coin
        for coin in coins:
            for i in range(coin, amount + 1):
                # is the previous route or current route less coins
                dp[i] = min(dp[i], dp[i-coin] + 1)

        # if we did not find a round to our amount with the given coins
        # return -1
        if dp[-1] > amount:
            return -1

        # otherwise return the least amount of coins to get to dp[-1]/dp[amount]
        return dp[-1]