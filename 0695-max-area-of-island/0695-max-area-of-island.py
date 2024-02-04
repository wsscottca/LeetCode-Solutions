'''
Timestamps:
    Cases: 1:00
    Design: 8:08
    Verify: 10:52
    Code: 16:41

Understand and cases:
    grid = [[1]]
    grid = [[0]]
    grid = [[1,0],[0,1]]
    
    [[1,1,0,0,0],
     [1,1,0,0,0],
     [0,0,0,1,1],
     [0,0,0,1,1]]

Design and verify:
    iterate through each cell
    if cell is an island
    check if explored
    if not, explore and count cells
    if larger than max, store
    return max at end
    
    max_area = 0
    visited = set()
    
    M = len(grid)
    N = len(grid[0])
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1 and (i,j) not in visited:
                area = 0
                to_visit = [(i,j)]
                
                while to_visit:
                    x, y = to_visit.pop()
                    visited.add((x,y))
                    area += 1
                    
                    for x_offset, y_offset in directions:
                        new_x = x + x_offset
                        new_y = y + y_offset
                        
                        if 0 <= new_x < M and 0 <= new_y < N and grid[new_x][new_y] == 1:
                            to_visit.append((new_x, new_y))
                    
                max_area = max(max_area, area)
    
    return max_area
                
                

'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # initialize our helpers, our max tracker, and our bounds
        max_area = 0
        visited = set()
        M = len(grid)
        N = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # for each cell in the grid
        for i in range(M):
            for j in range(N):
                # if it is an unvisited island
                if grid[i][j] == 1 and (i,j) not in visited:
                    # initalize this island's dfs and area counter
                    area = 0
                    to_visit = [(i,j)]
                    
                    # while we can explore the island (there are cells of the island to visit)
                    while to_visit:
                        # get our x and y, add it to our visited as a tuple, and increment our area
                        x, y = to_visit.pop()
                        
                        if (x,y) in visited:
                            continue
                        
                        visited.add((x,y))
                        area += 1
                        
                        # get our offsets for connected cells
                        for x_offset, y_offset in directions:
                            # get our new x and y after offsets
                            new_x = x + x_offset
                            new_y = y + y_offset
                            
                            # verify our new cell is in bounds, and check if it is still island and we haven't visited that cell
                            if 0 <= new_x < M and 0 <= new_y < N and grid[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                                # if it is we need to visit it
                                to_visit.append((new_x, new_y))
                    
                    # after our island has been explored and the area calculated, check if it is
                    # now the largest island
                    max_area = max(max_area, area)

        # finally return the largest island we found
        return max_area