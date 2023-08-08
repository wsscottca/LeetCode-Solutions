class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []      

        for token in tokens:
            # if the token is an operator, do the operation on the last 2 values
            if token == "+":
                stack.append(stack.pop() + stack.pop())

            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            
            # order matters for subtraction and division so store the last values
            elif token == "-":
                prev = stack.pop()
                two_prev = stack.pop()

                stack.append(two_prev - prev)

            elif token == "/":
                prev = stack.pop()
                two_prev = stack.pop()
                stack.append(int(two_prev / prev))
        
            # otherwise add the int to the stack
            else:
                stack.append(int(token))
        
        # result is the last item in the stack
        return stack.pop()