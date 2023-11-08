'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:

Understand and Cases:
    nums = [1]
    nums = [10,0,0,0,0,0,0,0]
    nums = [3,3,1,3,2,3,1]
    
Design and Verify:
    Keep track of largest difference while traversing our loop
    
    nlogn
    two pointers
    
    nlogn
    larger space
    recursive
    
    bottom up dp?
    
    dp = [-1 for _ in nums]
    dp[0] = 0
    each index lowest number of steps to get to that point
    for idx, num in enumerate(nums):
        for i in range(1, num + 1):
            if dp[idx + i] == -1:
                dp[idx + 1] = dp[idx] + 1
            
            dp[idx + i] = min(dp[idx + i], dp[idx] + 1)
    
    return dp[-1]
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        # bottom up dp, set arr to -1 as you cant have negative jumps
        # then initialize the first step to 0
        dp = [-1 for _ in nums]
        dp[0] = 0
        
        # each index lowest number of steps to get to that point
        # go through each number
        for idx, num in enumerate(nums):
            # and the steps it effects
            for i in range(1, num + 1):
                # ensure we're in bounds
                if idx + i > len(nums) - 1:
                    continue
                    
                # if we haven't reached it yet set the step to the current + 1
                if dp[idx + i] == -1:
                    dp[idx + i] = dp[idx] + 1
                    
                # only update if the current route is less steps than the existing
                dp[idx + i] = min(dp[idx + i], dp[idx] + 1)
                
                # if we reach the end we can assume it is the fastest route
                if dp[idx + i] == len(nums) - 1:
                    return dp[-1]
        
        # finally return our lowest number of steps to the end which is in our dp at the last spot
        return dp[-1]