'''
Timestamps:
    Understand and Cases: 1:00
    Design and Verify: 5:22
    Code:

Understand and Cases:
    nums = [1,1] target = 2
    nums = [1,2] target = 1
    nums = [4,1,3,2] target = 4
    
Design and Verify:
    dict
    add values with the indices as the value, and them as the key
    go through the dictionary
    check if the difference exist
        if it does, check that the index is different
    O(n)
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existing_nums = {}
        
        # Add all our values and the indices to our dictionary
        for idx, num in enumerate(nums):
            if num in existing_nums:
                existing_nums[num].append(idx)
            else:
                existing_nums[num] = [idx]
        
        print(existing_nums)
        
        # Go through each potential number
        for num in existing_nums.keys():
            diff = target - num
            
            # If we can reach target
            if diff in existing_nums:
                # Verify that we're not using the same number twice
                if diff == num:
                    if len(existing_nums[diff]) == 2:
                        return existing_nums[diff]
                    else:
                        continue
                
                # Otherwise if the numbers are different return their indices
                return [existing_nums[num][0], existing_nums[diff][0]]

        return [-1,-1]