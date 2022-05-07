public class Solution {
    public int RemoveDuplicates(int[] nums) {
        if (nums.Count() == 1) return 1;
        for (int i = 0; i < nums.Count(); i++)
        {
            if (i != Array.IndexOf(nums, nums[i]))
            {
                nums[i] = 101;
            }
        }
        Array.Sort(nums);
        if (Array.IndexOf(nums, 101) != -1) {
            return Array.IndexOf(nums, 101);
        }
        return nums.Count();
    }
}