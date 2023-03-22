class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left, right = 0, 1
        while right < len(prices):
            profit = prices[right] - prices[left]
            maxProfit = max(profit, maxProfit)
            
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                right += 1
                
        return maxProfit
            
            
                
            