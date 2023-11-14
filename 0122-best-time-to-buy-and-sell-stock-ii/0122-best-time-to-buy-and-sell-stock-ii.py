'''
Timestamps:
    Understand and Cases: 1:25
    Design and Verify: 4:30
    Code:
    
Understand and Cases:
    prices = [1]
    prices = [1,0,1,0]
    
Design and Verify:
    
    total_profit = 0
    for i in range(1, len(prices)):
        # if we can make a profit, do it
        if prices[i] > prices[i-1]:
            total_profit += prices[i] - prices[i-1]
    
    return total_profit
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for i in range(1, len(prices)):
            # if we can make a profit, do it
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]

        return total_profit