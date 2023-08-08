class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up dp - space efficient - requires 2 previous variables
        prev = 0
        two_prev = 0
        dp_max = 0
        
        for num in nums:
            # check if we should rob the current house or if the previous house was more profitable
            curr = two_prev + num
            dp_max = max(curr, prev)
            
            # set our prev values
            two_prev = prev
            prev = dp_max
        
        # return the last result
        return prev