class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[n] = 1
        
        for i in reversed(range(n)):
            if s[i] != "0":
                dp[i] = dp[i+1]
                
            if (i < n - 1) and (s[i] == "1" or s[i] == "2" and s[i + 1] <= "6"):
                dp[i] += dp[i + 2]
                
        return dp[0]