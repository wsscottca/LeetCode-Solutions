'''
Timestamps:
    Understand and Cases: 0:51
    Design and Verify: 6:19
    Code:

Cases:
    n = 0
    n = 1
    n = 5

Design and Verify:
    Space optimized bottom-up DP
    
    prev = 0
    two_prev = 1
    
    for i in range(1, n + 1):
        curr = prev + two_prev
        two_prev = prev
        prev = curr
    
    return prev
'''

class Solution:
    def fib(self, n: int) -> int:
        # intialize our starting values
        prev = 0
        two_prev = 1
        
        # for each int in between 1 and n (including n)
        for i in range(1, n + 1):
            # our current is the sum of our last two
            curr = prev + two_prev
            # then we update our last two
            two_prev = prev
            prev = curr
        
        # return prev as it was our most recent curr
        return prev