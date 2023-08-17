class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
            
        # use timestamp as the first element in tuple to do binary search in get
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.dict:
            return ""
        
        # as timestamps are increasing our list is sorted
        sorted_list = self.dict[key]
        
        left = 0
        right = len(sorted_list) - 1
        
        # perform binary search
        while left <= right:
            mid = (left + right) // 2
            
            if sorted_list[mid][0] == timestamp:
                return sorted_list[mid][1]
            
            elif sorted_list[mid][0] < timestamp:
                left = mid + 1
            
            else:
                right = mid - 1
                
        # if an exact timestamp is not found return the lower closest
        # which is our right as we have it cross over our left
        if sorted_list[right][0] > timestamp:
            return ""
        
        return sorted_list[right][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)