class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        
        sorted_intervals = sorted(intervals)
        for interval in sorted_intervals:
            if len(result) == 0 or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        
        return result