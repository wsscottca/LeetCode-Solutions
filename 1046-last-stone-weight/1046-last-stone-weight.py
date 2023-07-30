import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            biggest = -heapq.heappop(max_heap)
            second_biggest = -heapq.heappop(max_heap)
            
            if biggest != second_biggest:
                biggest -= second_biggest
                heapq.heappush(max_heap, -biggest)
        
        if not max_heap:
            return 0
        
        return -max_heap[0]