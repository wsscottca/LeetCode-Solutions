'''
Timestamps:
    Understand and Cases: 1:15
    Design and Verify:
    Code:
    
Understand and Cases:
    nums = [1,2,3,4]
    nums = [4,3,2,1]
    nums = [1,1,1,1]
    
Design and Verify:
    Naive O(n^2) for each int, find all following items
    Sort O(nlogn)
    
    O(2N)
    Add it to a set
    For each number check it's run if we haven't already visited it
    If it is longer than the current longest run, replace it
    
    # O(n) to turn the list to a set for O(1) operations
        numSet = set(nums)
        count = 0

        # for each number
        for num in nums:
            # if we have not already done the work
            if (num - 1) not in numSet:
                # start a new run
                runCount = 1
                while (num + runCount) in numSet:
                    runCount += 1;
                # store whether the new run is longer
                count = max(runCount, count)

        # return the longest run
        return count
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) to turn the list to a set for O(1) operations
        numSet = set(nums)
        count = 0

        # for each number
        for num in nums:
            # if we have not already done the work
            if (num - 1) not in numSet:
                # start a new run
                runCount = 1
                while (num + runCount) in numSet:
                    runCount += 1;
                # store whether the new run is longer
                count = max(runCount, count)

        # return the longest run
        return count