'''
Timestamps:
    Understand and Cases: 3:12
    Design and Verify:
    Code:
    
Cases:
    ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
    [[], [1], [1], [1], [], [1], []]
    
    ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom", "insert", "getRandom"]
    [[], [1], [2], [3], [], [3], [], [3], []]
    
Design:
    init:
        create an array and a dictionary
    
    insert:
        check if item is in dictionary, if it is store true else store false
        insert into array
        if it is in the dictionary add array index to index list of value
        otherwise add value to dictionary with array of just the index
        
    remove:
        check if the item is in the dictionary, if it isnt return false
        check what last item in the array is
        move an instance of the item to be removed with the item at the end (making sure to update our dictionary)
        remove the item from the end of the list
        return true
    
    get random:
        return random.choice(array)
'''
import random
class RandomizedCollection:

    def __init__(self):
        # initialize our data structures
        self.array = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        # if item is not already present get True to return
        res = True
        if val in self.dict:
            # if it is present get False to return
            res = False
            # then add it to our array
            # and add the index to our dict[val]
            index = len(self.array)
            self.array.append(val)
            self.dict[val].append(index)
            
        else:
            # add it to our array and set up our dict[val]
            index = len(self.array)
            self.array.append(val)
            self.dict[val] = [index]
        
        # return whether the item was not present
        return res
        

    def remove(self, val: int) -> bool:
        # check if the item exists to be removed
        if val not in self.dict:
            return False
        
        # get our last value/index so we can remove in O(1) as well as our index of the item to remove
        last = self.array[-1]
        last_index = len(self.array) - 1
        to_remove_index = self.dict[val][-1]
        
        # replace our last index with the new index of the item
        self.dict[last].remove(last_index)
        self.dict[last].append(to_remove_index)
        #remove it from our dict[val] index list
        self.dict[val].remove(to_remove_index)
        if not self.dict[val]:
            del self.dict[val]
        
        # replace the item in the array and then remove the last item
        self.array[to_remove_index] = last
        del self.array[-1]
        
        # return the success
        return True
        

    def getRandom(self) -> int:
        # return a random element in the array
        return random.choice(self.array)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom():