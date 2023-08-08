

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minimum = None
        
        # if the stack is empty, add the val and it is the min
        if not self.stack:
            self.stack.append((val, val))
            return
        
        # otherwise check if the current min (the min from the last tuple) is greater than val
        # if it is then set the new min (second index of tuple) to val
        if val < self.stack[-1][1]:
            minimum = val

        else:
            minimum = self.stack[-1][1]
        self.stack.append((val, minimum))
            

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()