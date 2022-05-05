public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int[] found;
        for (int i = 0; i < nums.Length; i++)
        {
            while (Array.IndexOf(nums, val) != -1)
            {
                nums[Array.IndexOf(nums, val)] = 101;
            }
        }
        Array.Sort(nums);
        if (Array.IndexOf(nums, 101) != -1) {
            return Array.IndexOf(nums, 101);
        }
        else if (nums.Length != 0)
        {
            return nums.Length;
        }
        else
        {
            return 0;
        }
    }
}