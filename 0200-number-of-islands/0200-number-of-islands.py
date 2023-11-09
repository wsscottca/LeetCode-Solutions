'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:
    
Understand and Cases:
    grid =  ["1", "1"],
            ["1", "1"]
        
    grid =  ["1", "0"],
            ["0", "1"]

Design and Verify:
    iterative + dfs
    
    count = 0
    visited = set()
    _dfs(node = (x, y)):
        visited.add(node)
        if grid[node[0]][node[1]] == "1":
            directions = [(0, 1), (1, 0)]
            for direction in directions:
                neighbor = node + direction
                if neighbor not in visited:
                    _dfs(neighbor)
                    
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "1" and (i, j) not in visited:
                count += 1
                _dfs((i, j))
                
    return count
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        def _dfs(node):
            visited.add(node)
            if grid[node[0]][node[1]] == "1":
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for direction in directions:
                    neighbor = (node[0] + direction[0], node[1] + direction[1])
                    if neighbor not in visited and 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                        _dfs(neighbor)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    _dfs((i, j))

        return count