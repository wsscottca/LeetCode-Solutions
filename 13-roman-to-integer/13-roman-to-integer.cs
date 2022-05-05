public class Solution {
    public int RomanToInt(string s) {
        Dictionary <int, int> counts = new Dictionary <int, int>();
        
        counts.Add(-100, 0);
        counts.Add(-10, 0);
        counts.Add(-1, 0);
        counts.Add(1, 0);
        counts.Add(5, 0);
        counts.Add(10, 0);
        counts.Add(50, 0);
        counts.Add(100, 0);
        counts.Add(500, 0);
        counts.Add(1000, 0);
        
        char next = 'A';
        
        for (int i = 0; i < s.Length; i++)
        {
            if (i+1 < s.Length)
            {
                next = s[i+1];
            }
            if (s[i] == 'I' && (next == 'V' || next == 'X'))
            {
                counts[-1] += 1;
            }
            else if (s[i] == 'X' && (next == 'L' || next == 'C'))
            {
                counts[-10] += 1;
            }
            else if (s[i] == 'C' && (next == 'D' || next == 'M'))
            {
                counts[-100] += 1;
            } else {
                switch(s[i])
                {
                    case 'I':
                        counts[1] += 1;
                        break;
                    case 'V':
                        counts[5] += 1;
                        break;
                    case 'X':
                        counts[10] += 1;
                        break;
                    case 'L':
                        counts[50] += 1;
                        break;
                    case 'C':
                        counts[100] += 1;
                        break;
                    case 'D':
                        counts[500] += 1;
                        break;
                    case 'M':
                        counts[1000] += 1;
                        break;
                }
            }
        }
        int sum = 0;
        foreach(KeyValuePair<int, int> kvp in counts)
        {
            sum += kvp.Key * kvp.Value;
        }
        return sum;
    }
}