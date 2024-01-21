'''
Timestamps:
    Cases: 1:20
    Design: 12:15
    Verify: 17:46
    Code:
    
Understand and Cases:
    nums = [1,1,1,1]
    nums = [0]
    nums = [2,0,2]

Design and Verify:
    cant divide
    prefix/suffix
    
    prefix [1,1,2,6]
    suffix [24,12,4,0]
    
    # get the product from the left
    prefix = [1]
    product = 1
    for i in range(1, len(nums)):
        product *= nums[i-1]
        prefix[i] = product
        
    # get the product from the right
    suffix = [1 for _ in nums]
    product = 1
    for i in range(len(nums)-2, -1, -1):
        product *= nums[i+1]
        suffix[i] = product
    
    # merge them for the overall product minus self
    res = []
    for i in range(len(nums)):
        res.append(prefix[i] * suffix[i])
    
    return res
        

'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get the product from the left
        prefix = [1 for _ in nums]
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            prefix[i] = product

        # get the product from the right
        suffix = [1 for _ in nums]
        product = 1
        for i in range(len(nums)-2, -1, -1):
            product *= nums[i+1]
            suffix[i] = product

        # merge them for the overall product minus self
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res