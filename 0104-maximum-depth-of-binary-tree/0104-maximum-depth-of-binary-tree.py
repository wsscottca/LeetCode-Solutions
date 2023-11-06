'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:

Understand and Cases:
    root = [1,1,null,1,null,null,null]
    root = [1]
    root = [1,1,1,1,1,null,1]
    
Design and Verify:
    DFS
    
    dfs(node):
        if not node:
            return 0
        
        height = max(node.left, node.right)
        
        return height + 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if there is no node, it cannot have a height
        if not root:
            return 0
        
        # calculate the heights of each child subtree, and get the max
        height = max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # the current height is the max child's height plus the current node
        return height + 1