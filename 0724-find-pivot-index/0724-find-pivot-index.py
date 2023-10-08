'''
Timestamps:
    Cases:
    Verify:
    Code:
    
Cases:
    nums = []
    nums = [0]
    nums = [-1,0,1]

Design and verify:
    if len(nums == 1):
        return 0
        
    left_sum = 0
    right_sum = sum(nums[1:])
    for i in range(len(nums) -  1):
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
        right_sum -= nums[i+1]
    
    if left_sum == right_sum:
        return i
    
    return -1
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left_sum = 0
        right_sum = sum(nums[1:])
        for i in range(len(nums) -  1):
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
            right_sum -= nums[i+1]

        if left_sum == right_sum:
            return i + 1

        return -1