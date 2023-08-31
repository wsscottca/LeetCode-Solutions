'''
Timestamps:
Understand - 5:00
Design and Verify - 10:00
Write Code

    1. Understand the problem
        3 other test cases:
            1. s = "(" - False - Correct
            2. s = "([)]" - False - Correct
            3. s = "([])" - True - Correct

    2. Design solution and verify solution 
        Create a dictionary of our close parenthesis and their matching opens
        Stack of open parenthesis

        For each parenthesis check if it is a close parenthesis
        If it is:
            Peek the stack
                If stack is empty return false
                If it is the matching open pop the open parenthesis
                If it is not matching return false
        If it is not:
            Add it to the stack
        
        If stack is not empty:
            return false
        
        return true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        
        # Check each token
        for paren in s:
            
            # Check if parenthesis is a closing parenthesis
            if paren in pairs.keys():
                # If it's a closing parenthesis and there is no opening it is invalid
                if not stack:
                    return False

                # Check if the open parenthesis is the proper one, if it is remove it, if not it is invalid
                if stack[-1] == pairs[paren]:
                    stack.pop()
                else:
                    return False
            
            # If it's an open parenthesis just push it to the stack
            else:
                stack.append(paren)
        
        # If the stack isn't empty there were not enough valid closes
        if stack:
            return False
        
        # If it has not been invalidated by oone of the prev tests it is valid
        return True
        