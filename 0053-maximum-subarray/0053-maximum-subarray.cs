public class Solution {
    public int MaxSubArray(int[] nums) {
        int max = int.MinValue,
            maxEnd = 0;
        foreach (int num in nums)
        {
            maxEnd = maxEnd + num;
            if (max < maxEnd)
                max = maxEnd;
            
            if (maxEnd < 0)
                maxEnd = 0;
        }
        return max;
    }
}