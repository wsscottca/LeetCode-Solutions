'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:

Understand and Cases:
    n = 4
    n = 1
    
Design and Verify:
    1   -   1
    2   -   2
    3   -   3
    4   -   5
    5   -   8
    
    
    
    two_prev = 0
    prev = 1
    
    # starting at 2, calculate the potential options
    # bases on the last two # of paths
    # recurrence relationship is dp[i] = dp[i-1] + dp[i-2]
    for i in range(1, n + 1):
        curr = two_prev + prev
        two_prev = prev
        prev = curr
    
    # return our prev which is our last variable
    return prev
        
    
    dp[i] = dp[i-1] + dp[i-2]
    
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        # store our last two calculations
        two_prev = 0
        prev = 1

        # starting at 2, calculate the potential options
        # bases on the last two # of paths
        # recurrence relationship is dp[i] = dp[i-1] + dp[i-2]
        for i in range(1, n + 1):
            curr = two_prev + prev
            two_prev = prev
            prev = curr

        # return our prev which is our last variable
        return prev