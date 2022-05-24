public class Solution {
    public int MaxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currSum = 0;
        foreach (int num in nums)
        {
            if (currSum < 0)
            {
                currSum = 0;
            }
            currSum += num;
            maxSum = Math.Max(maxSum, currSum);
        }
        return maxSum;
    }
}