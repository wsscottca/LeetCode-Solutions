'''
Timestamps:
    Cases: 1:20
    Design: 15:15
    Verify: 19:07
    Code:
    
Cases:
    n1 = [1,1,1,2,2,3,4] n2 = [4,5,6,7,8]
    n1 = [1] n2 = [2]
    n1 = [1,2,3] n2 = [1,2,3,4]

Design:
    Second attempt after studying
    
    Break into two partition, check the value
    
             l r
    nums1 = [1,3], nums2 = [2]
    nums1_mid = 0
    nums2_mid = -1
    nums1_left_part = 1
    nums1_right_part = 3
    nums2_left_part = -sys.maxsize
    nums2_right_part = 2
    
    overall = len(num1) + len(num2)
    half = overall // 2
    
    if len(num1) > len(num2):
        return findMedianSortedArrays(nums2, nums1)
        
    left = 0
    right = len(nums1) - 1
    
    while l <= r:
        nums1_mid = (l + r) // 2
        nums2_mid = half - nums1_mid - 2
        
        nums1_left_part = nums1[nums1_mid] if nums1_mid >= 0 else -sys.maxsize
        nums1_right_part = nums1[nums1_mid + 1] if (nums1_mid + 1) < len(nums1) else sys.maxsize
        nums2_left_part = num2[nums2_mid] if nums2_mid >= 0 else -sys.maxsize
        nums2_right_part = nums2[nums2_mid + 1] if (nums2_mid + 1) < len(nums2) else sys.maxsize
        
        if nums1_left_part <= nums2_right_part and nums2_left_part <= nums1_right_part:
            if overall % 2:
                return min(nums1_right_part, nums2_right_part)
            
            return (max(nums1_left_part, nums2_left_part) + min(nums1_right_part, nums2_right_part)) / 2
        
        elif nums1_left_part > nums2_right_part:
            right = nums1_left_part - 1
        
        else:
            left = nums1_left_part + 1
        
'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # store our overall length and half length for later calculations
        overall = len(nums1) + len(nums2)
        half = overall // 2
        
        # ensure our nums1 is the smaller list
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        # get our left and right value to find our first mid
        left = 0
        right = len(nums1) - 1
        
        # while we can continue searching
        while True:
            # our first mid is the mid of our l and r, our right mid is our half minus our first mid and pointers
            nums1_mid = (left + right) // 2
            nums2_mid = half - nums1_mid - 2

            # get the rightmost left partition values and leftmost right partition values, or set them to
            # -sys.maxsize or sys.maxsize so that on smaller arrays or lopsided ones our calculations still work
            nums1_left_part = nums1[nums1_mid] if nums1_mid >= 0 else -sys.maxsize
            nums1_right_part = nums1[nums1_mid + 1] if (nums1_mid + 1) < len(nums1) else sys.maxsize
            nums2_left_part = nums2[nums2_mid] if nums2_mid >= 0 else -sys.maxsize
            nums2_right_part = nums2[nums2_mid + 1] if (nums2_mid + 1) < len(nums2) else sys.maxsize
            
            # if both our lefts are smaller than both our rights we have found our median
            if nums1_left_part <= nums2_right_part and nums2_left_part <= nums1_right_part:
                # if it's odd return the smaller of the two
                if overall % 2:
                    return min(nums1_right_part, nums2_right_part)
                
                # otherwise calculate the median
                return (max(nums1_left_part, nums2_left_part) + min(nums1_right_part, nums2_right_part)) / 2
            
            # if we did not find our median, adjust our window based on which partition was not in proper order
            elif nums1_left_part > nums2_right_part:
                right = nums1_mid - 1

            else:
                left = nums1_mid + 1