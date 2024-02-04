'''
Timestamps:
    Cases: 1:58
    Design: 8:49
    Verify: 12:04
    Code:
    
Understand and Cases:
    s = "abcdefghijk"
    s = "abcabc"
    s = ""

Design and Code:
    sliding window
    
    if len(s) < 2:
        return len(s)
    
    longest = 0
    
    left = 0
    right = 0
    window = set()
    
    while right < len(s):
        if s[right] in window:
            if right-left+1 > longest:
                longest = right - left + 1
            
            while s[left] != s[right]:
                window.remove(s[left])
                left += 1
            
            left += 1
            continue
        
        window.add(s[right])
        right += 1
        
    return longest

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if theres 0 or 1 items, return that
        if not s or len(s) < 2:
            return len(s)
        
        # initialize helper, longest to store longest with no repeating
        # left and right for our window, window to store current window
        longest = 0
        left = 0
        right = 0
        window = set()

        # while we're in the array
        while right < len(s):
            # if we find a repeat
            if s[right] in window:
                # check if our current substring is the longest, if so update
                if right-left > longest:
                    longest = right - left
                # then move our left bound in until there's no repeat
                # removing anything not in our window
                while s[left] != s[right]:
                    window.remove(s[left])
                    left += 1

                left += 1
                right += 1
                continue

            # if there wasnt a repeat add the new character to the window
            # and move the right bound 
            window.add(s[right])
            right += 1

        # at the end return the length of the longest substr we found
        return max(longest, right-left)