class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        subarray_dict = {0:1}
        
        for num in nums:
            curr_sum += num
            if curr_sum - k in subarray_dict:
                count += subarray_dict[curr_sum - k]
                
            if curr_sum in subarray_dict:
                subarray_dict[curr_sum] += 1
            else:
                subarray_dict[curr_sum] = 1
        
        return count
                