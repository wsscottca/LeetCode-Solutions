'''
Timestamps:
    Understand and Cases: 2:05
    Design and Verify: 13:30
    Code:
    
Understand and Cases:
    prices = [1,1]
    prices = [0,1,0,1]
    prices = [0,1,0,0,1,2]
    
Design and Verify:
    Naive Recursive:
        Decision tree of buy/sell or cooldown (2^n)
    
    DP Memo:
        Decision tree, but store profits
        
    dict = {} (index, buying (state)) = max_profit
    _dfs(index, buying):
        if index >= len(prices[i]):
            return 0
        
        if buying:
            buy = dfs(i+1, not buying) - prices[i]
            cooldown = dfs(i+1, buying)
            dict[i, buying] = max(buy, cooldown)
        else:
            sell = dfs(i+2, not buying) + prices[i]
            cooldown = dfs(i+1, buying)
            dict[i, buying] = max(sell, cooldown)
            
        return dict[(i, buying)]
    
    _dfs(0, True)
    
    return dict[len(prices) - 1, True]
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dictionary memo to store already done work
        # (index, state (buying)) = max profit
        profits = {}
        
        # nested dfs to attempt both options at each point
        def _dfs(i, buying):
            if i >= len(prices):
                return 0
            
            # make sure we don't do extra work
            if (i, buying) in profits:
                return profits[(i, buying)]

            # if we're ing a buying state, check if it makes more sense to buy or cooldown
            # aka what is the max of each scenario
            if buying:
                buy = _dfs(i + 1, not buying) - prices[i]
                cooldown = _dfs(i+1, buying)
                profits[i, buying] = max(buy, cooldown)
            
            # if we're in a selling (not buying) state, check if it makes more sense to sell or cooldown
            # aka max of each scenario
            else:
                # if we see we need to cooldown so i+2
                sell = _dfs(i + 2, not buying) + prices[i]
                cooldown = _dfs(i + 1, buying)
                profits[i, buying] = max(sell, cooldown)

            return profits[(i, buying)]

        return _dfs(0, True)
    