'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:
    
Understand and Cases:
    nums = [1,0,1,0,1]
    nums = [1,2,1,5,6,1,1]

Design and Verify:
    DP bottom up
    
    
    def _path_max(arr) -> int:
        prev = arr[0]
        two_prev = 0
        
        for i in range(1, len(arr)):
            take = arr[i] + two_prev
            curr = max(take, prev)
            
            two_prev = prev
            prev = curr
        
        return prev
        
    return max(_path_max(arr[1::]), _path_max(arr[::-1]))
    
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        def _path_max(arr) -> int:
            prev = arr[0]
            two_prev = 0
            for i in range(1, len(arr)):
                take = arr[i] + two_prev
                curr = max(take, prev)
                
                two_prev = prev
                prev = curr

            return prev
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        return max(_path_max(nums[1::]), _path_max(nums[:-1]))