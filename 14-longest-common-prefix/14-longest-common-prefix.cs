public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        string answer = "";
        for (int i = 0; i < strs[0].Length; i++)
        {
            char test = strs[0][i];
            for (int j = 0; j < strs.Length; j++) {
                try {
                if (strs[j][i] == test)
                {
                    if (j == strs.Length - 1)
                    {
                        answer += strs[j][i];
                    }
                    continue;
                } else {
                    return answer;
                }
                } catch (IndexOutOfRangeException ex) {
                    return answer;
                }
            }
        }
        return answer;
    }
}