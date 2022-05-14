public class Solution {
    public int[] PlusOne(int[] digits) {
        int carry = 0;
        int start = 0;
        for (int i = digits.Count()-1; i >= 0; i--)
        {
            if (start == 0)
            {
                start = 1;
                if (digits[i] == 9)
                {
                    digits[i] = 0;
                    carry = 1;
                }
                else
                {
                    digits[i] += 1;
                    return digits;
                }
            }
            else if (carry == 1) 
            {
                    carry = 0;
                    digits[i]++;
                    if (digits[i] > 9)
                    {
                        digits[i] = 0;
                        carry = 1;
                    }
                    else
                    {
                        return digits;
                    }
            }
        }
        if (carry == 1)
        {
            int[] digitsNew = new int[digits.Count()+1];
            for (int i = 0; i < digitsNew.Count(); i++)
            {
                if (i == 0)
                {
                    digitsNew[i] = 1;
                }
                else
                {
                    digitsNew[i] = digits[i-1];
                }
            }
            return digitsNew;
        }
        return digits;
    }
}