public class Solution {
    public bool IsPalindrome(int x) {
        string xStr = x.ToString();
        for (int i = 0; i < xStr.Length; i++)
        {
            if(xStr[i] != xStr[xStr.Length-(i+1)])
            {
                return false;
            }
        }
        return true;
    }
}