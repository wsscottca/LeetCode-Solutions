'''
Timestamps:
    Understand and Cases: 2:00
    Design and Verify: 8:45
    Code: 
    
Understand and Cases:
    nums = [1,1,1,2,3,4,5,6,7,2,1,2,1,7]
    nums = [1,1,1]
    nums = [0,1,1]
    
Design and Verify:
    high = -sys.maxsize
    sec_high = -sys.maxsize
    third_high = -sys.maxsize
    
    high_neg = sys.maxsize
    sec_high_neg = sys.maxsize
    
    for num in nums:
        if num > third_high:
        
            if num > sec_high:
            
                if num > high:
                    third_high = sec_high
                    sec_high = high
                    high = num
                    continue
                    
                third_high = sec_high
                sec_high = num
                continue
                
            third_high = num
            continue
            
        if num < sec_high_neg:
            
            if num < high_neg:
                sec_high_neg = high_neg
                high_neg = num
                continue
            
            sec_high_neg = num
            continue
    
    return max(high * sec_high * third_high, sec_high_neg, high_neg, high)
'''

import sys
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Initialize our highs to the lowest possible
        high = -sys.maxsize
        sec_high = -sys.maxsize
        third_high = -sys.maxsize
        
        high_neg = sys.maxsize
        sec_high_neg = sys.maxsize

        # For each number
        for num in nums:
            # Check which if any high it is higher than
            if num > high:
                        # if it is the highest, cascade down the prev highest and second highest
                        third_high = sec_high
                        sec_high = high
                        high = num
                        
            elif num > sec_high:
                    # if it is the second highest, cascade down the prev second highest
                    third_high = sec_high
                    sec_high = num
                    
            elif num > third_high:
                # if it is the third highest, simply replace the prev third highest
                third_high = num
            
            # Also check if it is lower than our lowest two
            # As two negatives will produce a positive
            # if it is lower than both negs, move the prev high down and replace it
            if num < high_neg:
                sec_high_neg = high_neg
                high_neg = num
                
            elif num < sec_high_neg:
                # otherwise replace our second highest neg
                sec_high_neg = num
        
        
        neg_highest_product = sec_high_neg * high_neg * high
        highest_product = high * sec_high * third_high
            
        # Return the product of our highest numbers
        # or our highest cancelled out negatives and our highest number
        return max(highest_product, neg_highest_product)