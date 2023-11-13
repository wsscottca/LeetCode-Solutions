'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:
    
Understand and Cases:
    ["MyCalendar", "book", "book"]
    [[], [10, 15], [15, 25]]
    
    ["MyCalendar", "book", "book"]
    [[], [10, 15], [11, 12]]

Design and Verify:
    __init__():
        self.starts = []
        self.ends = []
        
    for i in range(starts):
        if (starts[i] <= start < ends[i]) or (starts[i] <= end <= ends[i]) or (start < starts[i] and end > ends[i]):
            return False
        
        starts.append(start)
        end.append(ends)
        return True

'''


class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.starts)):
            if (self.starts[i] <= start < self.ends[i]) or (self.starts[i] < end <= self.ends[i]) or (start < self.starts[i] and end > self.ends[i]):
                return False
        
        self.starts.append(start)
        self.ends.append(end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)