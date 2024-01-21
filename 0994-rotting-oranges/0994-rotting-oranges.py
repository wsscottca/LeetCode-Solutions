'''
Timestamps:
    Cases: 1:52
    Design: 13:35
    Verify: 19:38
    Code:
    
Cases:
    grid = [1]
    grid = [2]
    grid = [0]
    
Design and Verify:
    BFS
    
    q = deque()
    time, fresh = 0
    
    ROW, COL = len(grid), len(grid[0])
    for i in range(ROW):
        for j in range(COL):
            if grid[i][j] == 2:
                q.append([i,j])
            elif grid[i][j] == 1:
                fresh += 1
    
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    while q and fresh > 0:
        for i in range(len(q)):
            row, col = q.pop()

            for row_diff, col_diff in directions:
                new_row = row + row_diff
                new_col = col + col_diff

                if (0 <= new_row < ROW) and (0 <= new_col < COL):
                    if grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        q.append([new_row][new_col])
                        fresh -= 1
                        
        time += 1
    
    if fresh == 0:
        return time
        
    return -1       
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # intialize required data structures and variables
        queue = deque()
        time = 0
        fresh = 0
        
        # get our outter bounds
        ROW, COL = len(grid), len(grid[0])
        # Go through each cell
        for i in range(ROW):
            for j in range(COL):
                # if its rotten add it to the queue
                if grid[i][j] == 2:
                    queue.append([i,j])
                    
                # if its fresh add it to our fresh counter
                elif grid[i][j] == 1:
                    fresh += 1
        
        # helper variable for traversing each direciton
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        # while we have unvisited rotten and existing fresh
        while queue and fresh > 0:
            
            # only go through 1 turn at a time
            for i in range(len(queue)):
                # get the current coords
                row, col = queue.popleft()
                
                # get each neighboring coords
                for row_diff, col_diff in directions:
                    new_row = row + row_diff
                    new_col = col + col_diff
                    
                    # verify the new coords are in bounds
                    if (0 <= new_row < ROW) and (0 <= new_col < COL):
                        # if the cell is fresh, turn it rotten, add it to the queue
                        # and remove one from our fresh counter
                        if grid[new_row][new_col] == 1:
                            grid[new_row][new_col] = 2
                            queue.append([new_row, new_col])
                            fresh -= 1
            
            # at the end of each turn increment the time
            time += 1
        
        # if there are no fresh oranges left, return the amount of time 
        # it took to turn them all rotten
        if fresh == 0:
            return time
        
        # if there are still fresh we cannot turn them all
        return -1