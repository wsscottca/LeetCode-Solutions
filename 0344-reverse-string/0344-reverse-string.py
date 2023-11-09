'''
Timestamps:
    Understand and cases: 1:00
    Design and Verify:
    Code:
    
Understand and Cases:
    s = ["b", "o", "b"]
    s = ["N"]
    
Design and Verify:
    s.reverse()
    s[:] = s[::-1]
    
    String split then swap, then join
    Array of strings, don't have to split or join just swap
    
    Two pointers
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        # s[left], s[right] = s[right], s[left]
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        
        left += 1
        right -= 1
    
    return s
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Pointers that move inwards
        left = 0
        right = len(s) - 1
        
        # While we aren't in the middle
        while left < right:
            # Swap the characters from the left and right
            # s[left], s[right] = s[right], s[left]
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            
            # Increment/Decrement pointers
            left += 1
            right -= 1

        return s