class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        
        n = len(grid)
        m = len(grid[0])
        
        if n == 1 and m == 1:
            return 4
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i == 0:
                        perimeter += 1
                        
                    if i == n - 1:
                        perimeter += 1
                    
                    if j == 0:
                        perimeter += 1
                        
                    if j == m - 1:
                        perimeter += 1
                    
                    if (i + 1) < n and grid[i + 1][j] == 0:
                        perimeter += 1
                        
                    if (j + 1) < m and grid[i][j + 1] == 0:
                        perimeter += 1
                    
                else:
                    if (i + 1) < n and grid[i + 1][j] == 1:
                        perimeter += 1
                        
                    if (j + 1) < m and grid[i][j + 1] == 1:
                        perimeter += 1
                        
        return perimeter