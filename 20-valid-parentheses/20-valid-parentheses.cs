public class Solution {
    public bool IsValid(string s) {
        Stack<char> st = new Stack<char>();
        for(int i = 0; i < s.Length; i++)
        {
            switch (s[i])
            {
                    case '(':
                        st.Push(')');
                        break;
                    case '{':
                        st.Push('}');
                        break;
                    case '[':
                        st.Push(']');
                        break;
                    case ')':
                    case '}':
                    case ']':
                        if (st.Count == 0) {
                            return false;
                        }
                        else if (s[i] == st.Peek())
                        {
                            st.Pop();
                        }
                        else
                        {
                            return false;
                        }
                        break;
            }
        }
        if (st.Count == 0) {
            return true;
        }
        return false;
    }
}