'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:

Understand and Cases:
    m = 1 n = 1
    m = 2 n = 2
    
Design and Verify:
    dp bottom up
    start at grid[m-1][n-1]
    grid[m-1][n-1] = 1
    
    last_row = [6,3,1]
    
    
    
    last_row = [1 for _ in range(n)]
    
    for i in range(m-2, -1, -1):
        last_right = 1
        for j in range(n-2, -1, -1):
            last_row[j] += last_right
            
    return last_row[0]
                
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # store the last row for calulating
        # there is only 1 path as the robot can only move
        # right or down
        last_row = [1 for _ in range(n)]
        
        # for each cell in the grid other than the right and 
        # bottom borders, calculate the current number of paths
        for i in range(m-2, -1, -1):
            # we only need to store the last right but we need the
            # entire last row
            last_right = 1
            for j in range(n-2, -1, -1):
                # our current row (can write over last row)
                # is our bottom path count plus our right path count
                # aka same spot in last row, just add last_right
                last_row[j] += last_right
                
                # update last_right
                last_right = last_row[j]

        return last_row[0]