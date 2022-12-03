public class Solution {
    public bool IsSubsequence(string s, string t) {
        if (s.Length > t.Length) return false;
        if (s.Length == 0) return true;
        
        int sIndex = 0;
        for (int i = 0; i < t.Length; i++)
        {
            if (sIndex < s.Length && t[i] == s[sIndex])
            {
                sIndex++;
            }
        }
        return (sIndex == s.Length) ? true : false;
    }
}