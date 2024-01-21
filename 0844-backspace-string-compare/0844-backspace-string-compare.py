'''
Timestamps:
    Cases: 1:20
    Design: 4:40
    Verify: 7:20
    Code:

Understand and Cases:
    s = "#s" t = "s"
    s = "ss##" t = "s#s#"
    s = "sst##" t = "s#ts#"

Design and Verify:
    stack
    
    # remove all backspace characters
    # and characters to be removed
    def _remove_backspace(s):
        stack = []
        for char in s:
            if char == '#':
                if len(stack) > 1:
                    stack.pop()
            else:
                stack.append(char)
            
        return "".join(stack)
    
    # call our helper on both strings
    s = _remove_backspace(s)
    t = _remove_backspace(t)
    
    # compare the strings
    return if s == t
'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def _remove_backspace(s):
            stack = []
            for char in s:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)

            return "".join(stack)

        # call our helper on both strings
        s = _remove_backspace(s)
        t = _remove_backspace(t)

        # compare the strings
        return s == t