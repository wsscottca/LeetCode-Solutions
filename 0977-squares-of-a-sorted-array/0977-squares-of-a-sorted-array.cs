public class Solution {
    public int[] SortedSquares(int[] nums) {
        Stack<int> negs = new Stack<int>();
        int index = 0;
        foreach (int num in nums)
        {
            if (num < 0)
            {
                negs.Push(num * num);
            }
            else
            {
                int square = num * num;
                while (negs.Count > 0 && square >= negs.Peek())
                {
                    nums[index] = negs.Pop();
                    index++;
                }
                nums[index] = square;
                index++;
            }
        }
        while (negs.Count > 0)
        {
            nums[index] = negs.Pop();
            index++;
        }
        return nums;
    }
}