/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution : GuessGame {
    public int GuessNumber(int n) {
        int left = 1;
        int right = Int32.MaxValue;
        
        if(guess(left)==0) { return left; }
        if(guess(right)==0) { return right; }
        
        while (guess(n) != 0)
        {
            if (guess(n) == 1)
            {
                left = n;
                n = left + ((right - n) / 2);
            }
            else
            {
                right = n;
                n = right - (n - left) / 2;
            }
        }
        return n;
    }
}