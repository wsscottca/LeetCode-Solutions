'''
Timestamps:
    Understand & Test Cases: 3:00
    Design & Verify: 11:45
    Code:
    
Prework
    Understand & Test Cases:
        Extra Test Cases:
            nums = [] - invalid len(nums) > 0
            nums = [1,2,3,4] - [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4],[1,2,3,4]]
            nums = [2,-1] - [[],[2],[-1],[2,-1]]
    Design & Verify:
        Initial thoughts:
            Traverse
            
            initialize result List with empty list as only element
            for each number
                for each index in the current result list
                    add result[i] with the current number added to the end of result
                
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # initialize with empty set to build pattern
        res = [[]]
        
        # traverse each number
        for num in nums:
            
            # get the current number of sets outside our inner for loop
            # so that it doesn't go endlessly since we add to the result list
            curr_num_sets = len(res)
            
            # for each existing set add our current number to it then add it
            # to our result list as a new set
            for i in range(curr_num_sets):
                
                # if the index is an empty list/None create a list of just the new num
                if not res[i]:
                    new_set = [num]
                
                # otherwise create a copy of the set and add out new number to it
                else:
                    new_set = res[i].copy()
                    new_set.append(num)
                
                # add the new set to the results
                res.append(new_set)
        
        # return our list of sets
        return res