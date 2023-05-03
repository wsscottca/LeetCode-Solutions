import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        
        val = 0
        while len(nums) >= k:
            val = heappop(nums)
        
        return val
        