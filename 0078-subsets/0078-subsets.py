'''
Timestamps:
    Understand & Test Cases: 3:37
    Design & Verify: 11:45
    Code: 20:45
    
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
        res = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res