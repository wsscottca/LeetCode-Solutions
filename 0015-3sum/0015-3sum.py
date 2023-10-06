'''
Timestamps:
    Understand and Cases: 2:45
    Design and Verify: 18:40
    Code:
    
Cases:
    nums = [-1,0,0,1]
    nums = [-1,0,1,1]

Design:
    nlogn sort n^3
    
    sort
    res
    
    for i in range
        if nums[i] == nums[i-1]:
            continue
        
        left, right
        while left < right
            if nums[left] == prev:
                left += 1
                continue
            
            sum = nums[i] + nums[left] + nums[right]
            
            if sum == 0:
                res.append(nums[i], nums[left], nums[right])
                prev = nums[left]
                left += 1
            
            elif sum > 0:
                right -= 1
            
            else:
                prev = nums[left]
                left += 1
                
    return res
'''
import sys
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nlogn - makes it easier to work with
        nums.sort()
        res = []
        
        # for each item up to the third to last since we're working with triplets
        for i in range(len(nums) - 2):
            # if the current element is the same as the last, skip it as no dupes
            if i != 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            prev = sys.maxsize
            
            # two pointer similar to binary search, bring the window bounds in
            while left < right:
                # again stopping duplicates
                if nums[left] == prev:
                    left += 1
                    continue

                # have we reached our target?
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    prev = nums[left]
                    left += 1

                # if we need our sum smaller, move the right bound in
                elif curr_sum > 0:
                    right -= 1
                
                # otherwise move our left bound in
                else:
                    prev = nums[left]
                    left += 1
        # return the result
        return res