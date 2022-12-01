public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        Dictionary<int, int> valueCount = new Dictionary<int, int>();
        foreach (int num in nums)
        {
            if (valueCount.ContainsKey(num))
            {
                return true;
            }
            else
            {
                valueCount.Add(num, 1);
            }
        }
        return false;
    }
}