'''
Timestamps:
    Cases: 0:47
    Design: 4:18
    Verify: 7:14
    Code:

Cases:
    numbers = [1,2,3,5] target = 7
    numbers = [1,2] target = 3
    
Design:
    Dictionary using the indexes O(n) space and time
    Two pointer O(n) time, O(1) space
    
                 l   r   sum = 7
    numbers = [1,2,3,5] target = 7
    
    left = 0
    right = len(numbers - 1)
    
    while numbers[left] + numbers[right] != target:
        if numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1
    
    return [left + 1, right + 1]
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # pointer at the start and end
        left = 0
        right = len(numbers) - 1
        
        # until we find our target sum
        while numbers[left] + numbers[right] != target:
            # if the number is greater, move in the right bound
            if numbers[left] + numbers[right] > target:
                right -= 1
            # if it is lower, move in the left bound
            else:
                left += 1

        # as we're returning the number in line not index, add 1 to each so its 1 based not 0
        return [left + 1, right + 1]