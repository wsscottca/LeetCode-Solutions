public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        for (int i = 0; i < nums.Length; i++)
        {
            if (Array.IndexOf(nums, target - nums[i]) != -1 && Array.IndexOf(nums, target - nums[i]) != i)
            {
                return new int[] {i, Array.IndexOf(nums, target - nums[i])};
            }
        }
        return new int[] {0, 1};
    }
}