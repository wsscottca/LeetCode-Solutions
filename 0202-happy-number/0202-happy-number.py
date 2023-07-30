class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        
        while n != 1:
            if n in memo:
                return False
            
            memo.add(n)
            
            total = 0
            while n:
                total += (n % 10) * (n % 10)
                n = int(n / 10)
                
            n = total
        
        return True