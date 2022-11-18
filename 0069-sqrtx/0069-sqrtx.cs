public class Solution {
    public int MySqrt(int x) {
        if (x == 0) { return 0; }

        int left = 0;
        int right = 46340;

        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (mid * mid > x)
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
        return right;
    }
}