class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        res = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[i])
            res = max(res, i - left + 1)
        return res
                