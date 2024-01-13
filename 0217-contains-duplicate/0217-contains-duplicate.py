'''
Timestamps:
    Cases: 1:10
    Design: 2:20
    Verify: 4:15
    Code:

Cases:
    nums = [1,1,1]
    nums = [1,2]
    nums = [1]

Design and Verify:
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        
        set.add(num)
    
    return False
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set to store already seen ints
        seen = set()
        
        # for each int
        for num in nums:
            # check if we've seen it, if so there is a duplicate
            if num in seen:
                return True
            
            # otherwise add it to our set for future conditions
            seen.add(num)
        
        # if we've traversed all nums and not found a duplicate there is not one
        return False