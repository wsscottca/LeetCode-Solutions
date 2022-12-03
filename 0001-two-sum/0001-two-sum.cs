public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        for (int i = 0; i < nums.Length; i++)
        {
            int oppositeIndex = Array.IndexOf(nums, target - nums[i]);
            if (oppositeIndex != -1 && oppositeIndex != i)
            {
                return new int[] {i, oppositeIndex};
            }
        }
        return new int[] {0, 1};
    }
}