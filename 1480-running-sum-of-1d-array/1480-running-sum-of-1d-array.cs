public class Solution {
    public int[] RunningSum(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            count = count + nums[i];
            nums[i] = count;
        }
        return nums;
    }
}