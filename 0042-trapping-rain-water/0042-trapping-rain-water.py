'''
Timestamps:
    Understand and Cases: 2:00
    Design and Verify: 15:59
    Code:
    
Understand and Cases:
    height = [] # Not needed, at least one element
    height = [0, 5]
    height = [1,0,3,4,5]

Design and Verify:
    Naive = O(N^2)
    
    Two pointers:
        left, right
        left_max, right_max
        water
    
    water = 0
    
    # intialize bounds and intial max wall heights
    left = 0
    left_max = height[left]
    right = len(height) - 1
    right_max = height[right]
    
    # While we can lessen our window to find water
    while left < right:
        # Modify the lower wall
        if height[left] < height[right]:
            # if our wall gets taller, adjust our bound
            if height[left] > left_max:
                left_max = height[left]
            else:
                # otherwise check if we can contain more water
                water += left_max - height[left]
            # move our bound in
            left += 1
        
        else:
            # if our wall gets taller, adjust our bound
            if height[right] > right_max:
                right_max = height[right]
            else:
                # otherwise check if we can contain more water
                water += right_max - height[right]
            # move our bound in
            right -= 1
        
    # return the total water
    return water
    

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
    
        # intialize bounds and intial max wall heights
        left = 0
        left_max = height[left]
        right = len(height) - 1
        right_max = height[right]

        # While we can lessen our window to find water
        while left < right:
            # Modify the lower wall
            if height[left] < height[right]:
                # if our wall gets taller, adjust our bound
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    # otherwise check if we can contain more water
                    water += left_max - height[left]
                # move our bound in
                left += 1

            else:
                # if our wall gets taller, adjust our bound
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    # otherwise check if we can contain more water
                    water += right_max - height[right]
                # move our bound in
                right -= 1

        # return the total water
        return water