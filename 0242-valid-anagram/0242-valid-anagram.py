'''
Timestamps:
    Understand and Cases: 2:00
    Design and Verify: 6:51
    Code:
    
Understand and Cases:
    s = "IamLordVoldemort" t = "TomMarvoloRiddle"
    s = "bat" t = "rat"
    
Design and Verify:
    O(N)
    if len(s) != len(t):
        return False
        
    counts = defaultdict()
    for i in range(len(s)):
        counts[s[i]] += 1
    
    for i in range(len(t)):
        counts[t[i]] -= 1
        if counts[t[i]] < 0:
            return False
            
    return True
'''
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def default_value():
            return 0
        # Can't be an anagram if the lengths are different
        if len(s) != len(t):
            return False
        
        # Get character count of string
        counts = defaultdict(default_value)
        for i in range(len(s)):
            counts[s[i]] += 1
        
        # Count down character counts
        for i in range(len(t)):
            counts[t[i]] -= 1
            
            # If there is more instances of a letter than there should be, return false
            if counts[t[i]] < 0:
                return False

        return True