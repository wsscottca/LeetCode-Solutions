'''
Timestamps:
    Cases: 1:20
    Design: 2:30
    Verify: 3:09
    Code:
    
Cases:
    [1] 1
    [1] 0

Design and Verify:
    # pointers to define bounds of subarray as we narrow
    left = 0
    right = len(nums) - 1
    
    # while the bounds have not crossed
    while left < right:
        # get the mid val
        mid = (left + right) // 2
        
        # if we found target, return the index
        if nums[mid] == target:
            return mid
        
        # if the mid number is larger than our target
        # move our right bound in as the target is in the
        # left subarray
        elif nums[mid] > target:
            right = mid - 1
            
        # otherwise it's vice versa and in our right subarray
        else:
            left = mid + 1
    
    # if we exit our loop without finding the target it does not exist in our array
    return -1
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pointers to define bounds of subarray as we narrow
        left = 0
        right = len(nums) - 1

        # while the bounds have not crossed
        while left <= right:
            # get the mid val
            mid = (left + right) // 2

            # if we found target, return the index
            if nums[mid] == target:
                return mid

            # if the mid number is larger than our target
            # move our right bound in as the target is in the
            # left subarray
            elif nums[mid] > target:
                right = mid - 1

            # otherwise it's vice versa and in our right subarray
            else:
                left = mid + 1

        # if we exit our loop without finding the target it does not exist in our array
        return -1