import heapq

class MedianFinder:

    def __init__(self):
        self.upper_min_heap = []
        self.lower_max_heap = []

    def addNum(self, num: int) -> None:
        # if the upper half is not None and the given number belongs in the uppper half
        if self.upper_min_heap and num > self.upper_min_heap[0]:
            heapq.heappush(self.upper_min_heap, num)
        
        else:
            # switch to negative as heapq is min heap and using negatives makes it function as a max heap
            heapq.heappush(self.lower_max_heap, -num)
        
        lower_half = len(self.lower_max_heap)
        upper_half = len(self.upper_min_heap)
        
        if lower_half > (upper_half + 1):
            # pop from overfilled half
            inbalanced_num = heapq.heappop(self.lower_max_heap)
            # ensure to flip our negative back to positive when switching to our min heap
            heapq.heappush(self.upper_min_heap, -inbalanced_num)
            
        if upper_half > lower_half:
            # pop from overfilled half
            inbalanced_num = heapq.heappop(self.upper_min_heap)
            # ensure to flip to negative when switching to our max heap
            heapq.heappush(self.lower_max_heap, -inbalanced_num)
            

    def findMedian(self) -> float:
        # if the halves are equal the median is inbetween the max of the lower and the min of the upper
        if len(self.lower_max_heap) == len(self.upper_min_heap):
            # ensure to flip back to positive
            lower = -self.lower_max_heap[0]
            upper = self.upper_min_heap[0]
            
            return (upper + lower) / 2
        
        # otherwise our median is in our lower half as we keep it as the larger half
        else:
            # ensure to flip back to positive
            return -self.lower_max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()