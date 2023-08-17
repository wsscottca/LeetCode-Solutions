"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # If head node is none there is nothing to copy
        if not node:
            return None
        
        # Create a dictionary to store our visited nodes
        visited = {}
        def _dfs(node: 'Node') -> 'Node':
            if node.val in visited:
                return visited[node.val]
            
            new_node = Node(node.val)
            visited[node.val] = new_node
            
            for neighbor in node.neighbors:
                new_node.neighbors.append(_dfs(neighbor))
                
            return new_node
        
        _dfs(node)
        
        return visited[1]