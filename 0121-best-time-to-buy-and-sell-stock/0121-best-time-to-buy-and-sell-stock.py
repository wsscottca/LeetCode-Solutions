'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code and Debug:
    
Understand and Cases:
    prices = [1,1,1]
    prices = []
    prices = [2,1]
    prices = [1,2]
    prices = [1,2,3,4]
    
Design and Verify:
    Initial Thought:
        max var = 0
        
        if val at index 1 < val at index 0
            buy = second element
        else
            buy = first element
        
        iterate, looking at the next value
        
        if it is lower - calculate current max
            if current max is higher than max, set it
            if the low is lower than our buy, set our buy to it
        if it is higher or the same - ignore
        
        return max((last_item - buy), max)
        
        
'''
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0
        
        # set the initial buy
        buy = sys.maxsize
        
        # at each element check if we can have a lower buy
        # or if selling is a higher profit
        for price in prices:
            buy = min(buy, price)
            
            highest_profit = max(highest_profit, (price - buy))
                
        return highest_profit