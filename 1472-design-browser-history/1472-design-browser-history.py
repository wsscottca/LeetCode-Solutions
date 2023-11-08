'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:
    
Understand and Cases:
    ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
    [["google.com"],["a.com"],["b.com"],["c.com"],[1],[5],[1],["b.com"],[3],[1],[1]]
    
Design and Verify:
    __init__:
        store homepage
        store current page
        create stack for previous history
        create stack for forward history
        
    visit:
        add current page to previous history
        set current page to url
        empty forward_stack
    
    back:
        while prev_stack:
            if steps < 1:
                return current page
                
            add current page to forward history
            pull last page from prev_stack
            set current page to last page
            steps -= 1
        
        return current page
            
    forward:
        while forward_stack:
            if steps < 1:
                return current page
            
            add current page to prev_stack
            pull next page from forward_stack
            set current page to next page
            steps -= 1
        
        return current page
            

'''


class BrowserHistory:

    def __init__(self, homepage: str):
        # Initialize instance variables
        self.homepage = homepage
        self.curr_page = homepage
        self.prev_stack = []
        self.forward_stack = []

    def visit(self, url: str) -> None:
        # Empty the forward stack if it is populated
        # As there is now no forward history
        if self.forward_stack:
            self.forward_stack.clear()
        
        # Add the previous page to the prev stack
        self.prev_stack.append(self.curr_page)
        
        # Set the current page to the new page
        self.curr_page = url

    def back(self, steps: int) -> str:
        # While we can go back
        while self.prev_stack:
            # And we haven't gone further than requested
            if steps < 1:
                break
            
            # Add the current page to the forward history
            self.forward_stack.append(self.curr_page)
            
            # Remove the last page from the previous history
            # and set our current page to it
            self.curr_page = self.prev_stack.pop()
            
            # Keep track of steps
            steps -= 1
        
        # Return the ending page
        return self.curr_page

    def forward(self, steps: int) -> str:
        # While we can go forward
        while self.forward_stack:
            # And we haven't gone further than requested
            if steps < 1:
                break
            
            # Add the current page to the previous history
            self.prev_stack.append(self.curr_page)
            
            # Remove the next page from the forward history
            # and set our current page to it
            self.curr_page = self.forward_stack.pop()
            
            # Keep track of steps
            steps -= 1
        
        # Return the ending page
        return self.curr_page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)