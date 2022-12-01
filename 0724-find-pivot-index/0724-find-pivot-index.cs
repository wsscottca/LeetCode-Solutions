public class Solution {
    public int PivotIndex(int[] nums) {
        int middle = 0;
        while (middle < nums.Length)
        {
            int leftSum = 0;
            int rightSum = 0;

            for (int i = 0; i < nums.Length; i++)
            {
                if (i < middle)
                {
                    leftSum = leftSum + nums[i];
                }
                else if (i > middle)
                {
                    rightSum = rightSum + nums[i];
                }
            }
            if (leftSum == rightSum)
            {
                /**if (middle == nums.Length - 1)
                {
                    return 0;
                }
                else
                {*/
                    return middle;
                //}
            }
            middle++;
        }

        return -1;
    }
}