class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        m = len(heights)
        n = len(heights[0])
        
        def dfs(visited, x, y):
            visited.add((x, y))
            
            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]
                
                if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in visited and heights[newX][newY] >= heights[x][y]:
                    dfs(visited, newX, newY)
                    
        for i in range(m):
            dfs(pacific, i, 0)
            dfs(atlantic, i, n-1)
            
        for i in range(n):
            dfs(pacific, 0, i)
            dfs(atlantic, m-1, i)
            
        return list(pacific.intersection(atlantic))
            
        
        