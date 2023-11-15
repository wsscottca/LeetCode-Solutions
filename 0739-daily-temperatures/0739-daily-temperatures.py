'''
Timestamps:
    Understand and Cases:
    Design and Verify:

Understand and Cases:
    temperatures = [30]
    temperatures = [30,31,30,31,30]
    
Design and Verify:
    Going forward and searching for next highest O(n^2)
    Store what we've passed, and then calculate backwards
    
    
    stack = []
    ans = [0 for _ in range(len(temperatures))]
    
    for i, temp in enumerate(temperatures):
        # pop out all the previous temperatures that are lower then the current
        # and update their steps in our ans
        while stack and temperatures[stack[-1]] < temp:
            lower_idx = stack.pop()
            ans[lower_idx] = i - lower_idx
            
        # ensure we add the current value to the stack for future processing
        stack.append(i)
    
    return ans
'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack to hold prev window
        stack = []
        # preloading our answer with 0s
        ans = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            # pop out all the previous temperatures that are lower then the current
            # and update their steps in our ans
            while stack and temperatures[stack[-1]] < temp:
                lower_idx = stack.pop()
                ans[lower_idx] = i - lower_idx

            # ensure we add the current value to the stack for future processing
            stack.append(i)

        return ans