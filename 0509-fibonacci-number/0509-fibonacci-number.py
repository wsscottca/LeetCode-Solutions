class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        two_before = 1
        one_before = 1
        
        for i in range(2,n):
            if i % 2 == 0:
                two_before = two_before + one_before
            else:
                one_before = two_before + one_before

        return max(one_before, two_before)