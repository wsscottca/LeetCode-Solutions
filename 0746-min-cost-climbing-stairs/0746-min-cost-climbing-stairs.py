'''
Timestamps:
    Cases: 1:00
    Design: 4:15
    Verify: 7:41
    Code: 8:27
    
Understand and cases:
    cost = [1,2]
    cost = [1,1,1,1,1,1]
    cost = [1,4,5,2,5,6,3,7]
    
Design and verify:
    DP bottom up
    
    # if the length is exactly two we can't
    # build our DP solution so return the lesser
    if len(cost) == 2:
        return min(cost[0], cost[1])
    
    # initialize helpers
    two_prev_low = cost[0]
    prev_low = cost[1]
    
    # for each cost from 3rd (2 index) to end
    for i in range(2, len(cost)):
        # curr is the lesser of the last 2 costs (since we can step 1 or 2)
        # plus the current cost
        curr = cost[i] + min(two_prev_low, prev_low)
        
        # update helpers
        two_prev_low = prev_low
        prev_low = curr
    
    # return the min of the 2 prev lows
    return min(prev_low, two_prev_low)
'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # if the length is exactly two we can't
        # build our DP solution so return the lesser
        if len(cost) == 2:
            return min(cost[0], cost[1])

        # initialize helpers
        two_prev_low = cost[0]
        prev_low = cost[1]

        # for each cost from 3rd (2 index) to end
        for i in range(2, len(cost)):
            # curr is the lesser of the last 2 costs (since we can step 1 or 2)
            # plus the current cost
            curr = cost[i] + min(two_prev_low, prev_low)

            # update helpers
            two_prev_low = prev_low
            prev_low = curr

        # return the min of the 2 prev lows
        return min(prev_low, two_prev_low)