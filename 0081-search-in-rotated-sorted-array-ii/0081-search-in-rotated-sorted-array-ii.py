'''
Timestamps:
    Understand and Case: 2:22
    Design and Verify: 13:12
    Code:
    
Understand and Cases:
    nums = [1] target = 1
    nums = [1] target = 2
    nums = [2,3,1] target = 3
    
Design and Verify:
    binary search
    start at half
    
    while left < right
        check if our mid is the target, if it is return true
        if mid > target:
            check if left is < mid:
                if it is that is the sorted half
                if not check if target is less than right:
                    if it is the target is in the right sorted subarray
                    if not target is in the unsorted left subarray
        otherwise
            check if right is > mid
                if it is that is the sorted half
                if not check if target is greater than left:
                    if it is the target is in the left sorted subarray
                    if not target is in the unsorted right subarray
    
    if we exit our loop it is not in array so return false
'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            elif nums[left] == nums[mid] and nums[left] == nums[right]:
                i = left
                while i < len(nums) and nums[i] == nums[left]:
                    i += 1
                    
                if i == len(nums):
                    return False
                
                left = i
            
            elif nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return False
        