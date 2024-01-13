'''
Timestamps:
    Cases: 1:40
    Design: 10:37
    Verify: 15:24
    Code:
    
Cases:
    nums = [1] target = 1
    nums = [1,2,2,4,5,5] target = 4
    nums = [1,1,1,1,1,1,1,1] target = 1
    
Design:
    linear O(n)
    two pointer O(n)
    3x binary search (target, first, last)
    
    find the target using binary search
    def _findTarget(left, right):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                left = _findStart(left, mid)
                right = _findEnd(mid, right)

                return [left, right]

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1
        
        return [-1,-1]
            
    find the first instance of the target if we found the target
    modified binary search
    def _findStart(left, right):
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                if mid == 0:
                    return mid
                    
                if nums[mid-1] != target:
                    return mid
                    
                else:
                    right = mid - 1
                

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1
                
    find the last instance of the target if we found the target
    modified binary search
    def _findEnd(left, right):
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                if mid == len(nums) - 1:
                    return mid
                    
                if nums[mid+1] != target:
                    return mid
                    
                else:
                    left = mid + 1
                

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1
            
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find the target using binary search
        def _findBounds(left, right):
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    left = _findStart(left, mid)
                    right = _findEnd(mid, right)

                    return [left, right]

                elif nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return [-1,-1]

        # find the first instance of the target if we found the target
        # modified binary search
        def _findStart(left, right):
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    # ensure we aren't at the bounds of nums
                    if mid == 0:
                        return mid
                    
                    # if the number before our mid is not the target we found
                    # the bounds of our target
                    if nums[mid-1] != target:
                        return mid

                    else:
                        right = mid - 1


                elif nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

        # find the last instance of the target if we found the target
        # modified binary search
        def _findEnd(left, right):
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    # ensure we aren't at the bounds of nums
                    if mid == len(nums) - 1:
                        return mid
                    
                    # if the number before our mid is not the target we found
                    # the bounds of our target
                    if nums[mid+1] != target:
                        return mid

                    else:
                        left = mid + 1


                elif nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1
            
        return _findBounds(0, len(nums)-1)