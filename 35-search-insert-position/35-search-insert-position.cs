public class Solution {
    public int SearchInsert(int[] nums, int target) {
        for (int i = 0; i < nums.Count(); i++)
        {
            if (nums[i] == target)
            {
                return i;
            }
            else if (nums[i] > target) {
                return i;
            }
            else if (i == nums.Count() - 1)
            {
                return nums.Count();
            }
        }
        return 0;
    }
}