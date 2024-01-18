'''
Timestamps:
    Cases: 1:20
    Design: 6:10
    Verify: 7:25
    Code: 9:55
    
Understand and Cases:
    ["Solution", "shuffle", "reset", "shuffle"] #equal chance of 1,2 and 2,1
    [[[1, 2]], [], [], []]

    ["Solution", "shuffle", "reset", "shuffle"] # always 1
    [[[1]], [], [], []]



Design and Verify:
    store original array
    
    init:
        self.arr = nums
        
    reset:
        return self.arr
        
    # for each item, randomly swap it with another item
    shuffle:
        res = self.arr
        for i in range(len(res)):
            j = random.choice(range(len(res)))
            temp = res[i]
            res[i] = res[j]
            res[j] = res[i]
        
        return res

'''


class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def reset(self) -> List[int]:
        return self.arr

    def shuffle(self) -> List[int]:
        # create a copy so we always have the original
        res = self.arr.copy()
        
        # for each item, randomly swap it
        for i in range(len(res)):
            j = random.choice(range(len(res)))
            temp = res[i]
            res[i] = res[j]
            res[j] = temp
        
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()