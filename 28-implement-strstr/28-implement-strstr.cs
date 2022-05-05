public class Solution {
    public int StrStr(string haystack, string needle) {
        if(haystack != "" && needle != "")
        {
            return haystack.IndexOf(needle);
        }
        return 0;
    }
}