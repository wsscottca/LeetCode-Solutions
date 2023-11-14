'''
Timestamps:
    Understand and cases: 1:35
    Design and Verify:
    Code:
    
Understand and Cases:
    s = "ab"
    s = "aaaaabda"
    s = "aaabvdaaaa"

Design and Verify:
    checks if index has a palindrome
    treat as its the middle of the palindrome
    
    def expand(l, r):
        # while we're in bounds and the items match
        while l > 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        # return the length of the palindrome
        return r - l + 1
        
    max_length = 0
    start = 0
    
    for i in range(len(s)):
        # get the lengths of if the current char
        # is the middle or shared middle
        odd_length = expand(i,i)
        even_lenth = expand(i, i+1)
        
        # if we found a larger palindrome find it's start
        # based on if it's even or odd
        # and set our new max_length
        if max(odd_length, even_length) > max_length:
            if odd_length > even_length:
                start = i - (odd_length // 2)
            else:
                start = i - (even_length // 2) + 1
                
            max_length = max(odd_length, even_length)
    
    # get the last index of the palindrome so we can slice the string
    end = start + max_length - 1
    return s[start:end]
        
    
    
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            # while we're in bounds and the items match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                
            # return the length of the palindrome
            return s[l+1:r]

        longest_palindrome = ""

        for i in range(len(s)):
            # if the current char is the middle or shared middle
            # get the length of the potential palindrome
            odd = expand(i, i)
            even = expand(i, i+1)
            
            # if we found a larger palindrome 
            # save it and it's length
            if max(len(odd), len(even)) > len(longest_palindrome):
                if len(odd) > len(even):
                    longest_palindrome = odd
                else:
                    longest_palindrome = even
                

        # return the longest palindrome we found
        return longest_palindrome