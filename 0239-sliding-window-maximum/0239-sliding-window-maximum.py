'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:
    
Understand and Cases:
    nums = [1,2,3,4,5,6] k = 6
    nums = [6,5,4,3,2,1] k = 3
    nums = [1,2,3,4,5,6] k = 1
    
Design and Verify:
    Did before (3 days ago), completed but runtime was too slow O(nlogn)
    Anything previous that is less is not needed
    deque
    
    O(n)
    window = [7]
    maxes = [3, 3, 5, 5, 6, 7]
    i = 7
    
    window = collections.deque()
    maxes = []
    
    for i, num in enumerate(nums):
        # if we have numbers in our deque that are useless
        # as in they will never be the max, remove them
        if window and nums[window[-1]] < num:
            window.pop()
        
        # remove previous max if it leaves the window
        if window and window[0] < i - k + 1
            window.popleft()
        
        window.append(i)
        
        if i >= k - 1:
            maxes.append(nums[window[0]])
    
    return maxes
    
'''


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque so we cant O(1) both sides
        window = collections.deque()
        maxes = []

        for i, num in enumerate(nums):
            # if we have numbers in our deque that are useless
            # as in they will never be the max, remove them
            while window and nums[window[-1]] < num:
                window.pop()

            # remove previous max if it leaves the window
            if window and window[0] < i - k + 1:
                window.popleft()
            
            # add the element to the window
            window.append(i)
            
            # only add max if we've gotten to our window size
            if i >= k - 1:
                maxes.append(nums[window[0]])
        
        return maxes