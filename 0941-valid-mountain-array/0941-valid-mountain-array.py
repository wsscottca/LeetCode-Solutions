'''
Timestamps:
    Cases: 1:15
    Verify:
    Code:
    
Understand and Cases:
    arr = [1,1,1]
    arr = [1,2,1]
    arr = [1,1,2]
    
Design and verify:

    
    
    if len(arr) < 3:
        return False
    
    last_index = len(arr) - 1
    
    pointer = arr[0]
    # climb the mountain
    while pointer < last_index and arr[pointer + 1] > arr[pointer]:
        pointer += 1
    
    # leave the mountain
    while pointer < last_index and arr[pointer + 1] < arr[pointer]:
        pointer += 1
        
    return pointer == last_index
    
'''


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        last_index = len(arr) - 1
        climbed = False
        declined = False
        
        pointer = 0
        # climb the mountain
        while pointer < last_index and arr[pointer + 1] > arr[pointer]:
            climbed = True
            pointer += 1
        
        # leave the mountain
        while pointer < last_index and arr[pointer + 1] < arr[pointer]:
            declined = True
            pointer += 1
        
        return climbed and declined and pointer == last_index