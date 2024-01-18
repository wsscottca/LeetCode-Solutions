'''
Timestamps:
    Cases: 2:10
    Design: 12:45
    Verify: 14:15
    Code:
Understand and Cases:
    grid = [0, 0], [0, 1]
    grid = [0, 0], [0, 0]
    grid = [0, 1], [1, 0]

Design and Verify:
    dp bottom up
    space optimized
    store last row
    
    last_row = [0,0]
    
    m = len(grid)
    n = len(grid[0])
    
    # if there is an obstacle in our exit, there are no valid paths
    if grid[m - 1][n - 1] == 1:
        return 0
    
    # at any point our last_row will hold the last row
    # we visited and the progress of the current row
    last_row = [0 for _ in range(n)]
    last_row[n-1] = 1
    
    # for each grid cell, working from the exit
    for i in range(m, 0, -1):
        for j in range(n, 0, -1):
            # if there is an obstacle, there are no paths to that point
            if grid[i][j] == 1:
                last_row[j] = 0
                break
            
            # if no obstacle, check if we're in the last column
            # if we are last_row[j] stays the same as it only adds
            # the below path count which is the current last_row[j]
            if j < n:
                # otherwise our last_row[j] is the path count from both the
                # below (existing last_row[j]) and the right (last_row[j+1])
                last_row[j] = last_row[j + 1] + last_row[j]
    
    return last_row[0]
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # if there is an obstacle in our exit, there are no valid paths
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # at any point our last_row will hold the last row
        # we visited and the progress of the current row
        last_row = [0 for _ in range(n)]
        last_row[n-1] = 1

        # for each grid cell, working from the exit
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # if there is an obstacle, there are no paths to that point
                if obstacleGrid[i][j] == 1:
                    last_row[j] = 0
                    continue

                # if no obstacle, check if we're in the last column
                # if we are last_row[j] stays the same as it only adds
                # the below path count which is the current last_row[j]
                if j < n-1:
                    # otherwise our last_row[j] is the path count from both the
                    # below (existing last_row[j]) and the right (last_row[j+1])
                    last_row[j] = last_row[j + 1] + last_row[j]

        return last_row[0]