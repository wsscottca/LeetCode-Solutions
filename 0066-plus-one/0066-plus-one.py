'''
Timestamps:
    Cases: 1:30
    Design: 7:45
    Verify: 8:30
    Code:

Understand and Cases:
    digits = [1]
    digits = [9,9,9]
    digits = [1,2,9]

Design and Verify:
    start at end and increment, accounting for carries
    
    [1,0,0,0]
    
    # For each int working backwards
    for i in range(len(digits) - 1, -1, -1):
        # if the int is not a 9 we add 1 and return
        if digits[i] != 9:
            digits[i] += 1
            return digits
            
        # if the int is 9, set it to 0 and we carry the one
        # by continuing
        digits[i] = 0
        
        # if we reach the front and there is a 9
        # add 1 to the front of the array after setting the front
        # to 0 and then return
        if i == 0:
            return [1] + digits
            
    return -1
        
        
        
    

'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # For each int working backwards
        for i in range(len(digits) - 1, -1, -1):
            # if the int is not a 9 we add 1 and return
            if digits[i] != 9:
                digits[i] += 1
                return digits

            # if the int is 9, set it to 0 and we carry the one
            # by continuing
            digits[i] = 0

            # if we reach the front and there is a 9
            # add 1 to the front of the array after setting the front
            # to 0 and then return
            if i == 0:
                return [1] + digits

        return -1