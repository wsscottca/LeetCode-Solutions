import random

class RandomizedSet:

    def __init__(self):
        self.map = dict()
        self.list = []
        
        self.count = 0
        
    def insert(self, val: int) -> bool:
        if val in self.map.keys():
            print(self.map)
            return False
        
        self.map[val] = self.count
        self.list.append(val)

        self.count += 1
        
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map.keys():
            return False
        
        if len(self.map.keys()) == 1:
            self.map = {}
            self.list = []
            self.count -= 1
            return True
        
        index = self.map[val]
        last = self.list[-1]
        
        print(val, self.count, index)
        self.list[-1] = self.list[index]
        self.list[index] = last
        self.list.pop()
        
        self.map[last] = index
        self.map.pop(val)
        self.count -= 1
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()