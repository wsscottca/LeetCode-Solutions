class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        last_two = (1,1)
        for i in range(2, n):
            curr = last_two[0] + last_two[1]
            last_two = (curr, last_two[0])

        return last_two[0]