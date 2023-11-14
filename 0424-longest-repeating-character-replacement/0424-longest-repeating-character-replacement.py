'''
Timestamps:
    Understand and Cases: 1:40
    Design and Verify: 18:56
    Code:
    
Understand and Cases:
    s = "ABABA", k = 0
    s = "ABABA", k = 5
    
Design and Verify:
    count
    sliding window
    
    
    freq = { A: 2, B: 3 }
    most_common = 3
    mismatch = 2
    max_len = 4
    
    # default value for default dict
    def default_val():
        return 0
    
    # dictionary to store the count of each char
    freq = collections.defaultdict(default_val)
    left = 0
    max_len = 1
    
    for right in range(1, len(s) + 1):
        # add current char to freq dict
        freq[s[right - 1]] += 1
        
        # find the most common char in our window
        most_common = max(freq.values())
        
        # find the number of characters that are NOT our char
        mismatch = right - left - most_common
        
        # if this number is greater than k, we need to move our window
        if mismatch > k:
            freq[s[left]] -= 1
            left += 1
        
        # save the largest working window
        max_len = max(right - left, max_len)
    
    return max_len

'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # default value for default dict
        def default_val():
            return 0

        # dictionary to store the count of each char
        freq = collections.defaultdict(default_val)
        left = 0
        max_len = 1

        for right in range(1, len(s) + 1):
            # add current char to freq dict
            freq[s[right - 1]] += 1

            # find the most common char in our window
            most_common = max(freq.values())

            # find the number of characters that are NOT our char
            mismatch = right - left - most_common

            # if this number is greater than k, we need to move our window
            if mismatch > k:
                freq[s[left]] -= 1
                left += 1

            # save the largest working window
            max_len = max(right - left, max_len)

        return max_len