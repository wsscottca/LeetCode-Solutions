class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        n = len(s)
        curr = 0
        last = 1
        two_prev = 0
        
        for i in reversed(range(n)):
            curr = 0
            if s[i] != "0":
                curr = last
                
            if (i < n - 1) and (s[i] == "1" or s[i] == "2" and s[i + 1] <= "6"):
                curr += two_prev
                
            two_prev = last
            last = curr
            
                
        return curr