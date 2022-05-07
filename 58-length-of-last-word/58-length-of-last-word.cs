public class Solution {
    public int LengthOfLastWord(string s) {
            while (s.LastIndexOf(' ') == s.Length - 1 && s.Length > 1)
            {
                s = s.Substring(0, s.Length - 1);
            }
        if (s.IndexOf(' ') != -1)
        {
            s = s.Substring(s.LastIndexOf(' ') + 1);
        }
        return s.Length;
    }
}