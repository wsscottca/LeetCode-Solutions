'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:
    
Understand and Cases:
    nums = [1]
    nums = [0,1,1,2,5,6,3,4,5]
    
Design and Verify:
    Recursive - check every "path" O(2^N) and large space
    DP - Lower space of Recursive
    Store sequence in array, and modify it if a lower item is found?
    logn option (binary or heap)
    
    [3,5,6,2,5,4,19,5,6,7,12]
    ans = [3,5,6]
          [3, 10]
          [3, 8]
          [3, 8, 9]
    
    ans = [nums[0]]
    for num in nums:
        # if it is greater than the last number in our
        # sequence, add it to our sequence
        if num > ans[-1]:
            ans.append(num)
            
        else:
            # binary to find where in our sequence the number would go
            left = 0
            right = len(ans) - 1
            
            while left < right:
                mid = (left + right) // 2
                if ans[mid] == num:
                    left = mid
                    break
                elif ans[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # replace the left number (the greater once we exit)
            # to preserve order
            # essentially we are going back, and replacing the path 
            # we made and seeing if a longer path will present
            # if it doesn't since we are only concerned with the length not
            # the actual path it doesn't matter that we wrote over it
            ans[left] = num
                    
    return len(ans)
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for num in nums:
            # if it is greater than the last number in our
            # sequence, add it to our sequence
            if num > ans[-1]:
                ans.append(num)

            else:
                # binary to find where in our sequence the number would go
                left = 0
                right = len(ans) - 1

                while left <= right:
                    mid = (left + right) // 2
                    if ans[mid] == num:
                        left = mid
                        break
                    elif ans[mid] > num:
                        right = mid - 1
                    else:
                        left = mid + 1

                # replace the left number (the greater once we exit)
                # to preserve order
                # essentially we are going back, and replacing the path 
                # we made and seeing if a longer path will present
                # if it doesn't since we are only concerned with the length not
                # the actual path it doesn't matter that we wrote over it
                ans[left] = num

        return len(ans)