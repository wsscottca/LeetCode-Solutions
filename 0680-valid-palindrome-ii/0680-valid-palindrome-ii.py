'''
Timestamps:
    Cases: 1:51
    Design: 5:00
    Verify: 7:00
    Code: 7:30
    
Understand and Cases:
    s = "a"
    s = "ab"
    s = "abc"

Design and Verify:
    left = 0
    right = len(s) - 1
    
    used_delete = false
    
    while left > right:
        if s[left] != s[right] and used_delete:
            return False
        elif s[left] != s[right]:
            if s[left + 1] == s[right]:
                left += 1
            elif s[right - 1] == s[left]:
                right -= 1
            else:
                return False
                
            used_delete = True
        
        left += 1
        right -= 1
        
    return True

'''

'''
           012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
 0123456789111111111122222222223333333333444444444455555555556666666666777777777788888888889999999999
"aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def two_pointer_valid_palin(s, left, right, used_delete):
            # while our pointers haven't crossed
            while left < right:
                # if the left and right pointers values don't match
                if s[left] != s[right]:
                    # if we've used our delete it is not valid
                    if used_delete:
                        return False

                    # otherwise check if removing the left or right character results in a valid palindrome
                    else:
                        return two_pointer_valid_palin(s, left+1, right, True) or two_pointer_valid_palin(s, left, right-1, True)
                else:
                    left += 1
                    right -= 1
        
            # if we haven't found an unsolvable mismatch then
            # we can return True
            return True
        return two_pointer_valid_palin(s, 0, len(s)-1, False)