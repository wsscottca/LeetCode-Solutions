'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:
    
Understand and Cases:
    n = 10000, bad = 7689
    n = 1, bad = 1
    
Design and Verify:
    Binary Search
    
    
    if n == 1:
        return 1
        
    left = 1
    right = n
    
    while left < right:
        mid = (right + left) // 2
        if isBadVersion(mid):
            if not isBadVersion(mid - 1) or mid == 1:
                return mid
            right = mid - 1
        else:
            left = mid + 1
            
    return left
        
'''


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # If there is only 1 version, it is the bad version
        if n == 1:
            return 1
        
        # Set our bounds
        left = 1
        right = n

        # Essentially while we haven't searched everything
        while left < right:
            mid = (right + left) // 2
            
            # Move our bounds based on if the mid version is bad
            if isBadVersion(mid):
                # If our mid is the first bad version or the first element
                # return it
                if not isBadVersion(mid - 1) or mid == 1:
                    return mid
                
                right = mid - 1
            else:
                left = mid + 1
        
        # If we've done our search, the left is always the bad version
        # as it swaps with the right if it is at the edge of the bad
        # versions to break the loop
        return left