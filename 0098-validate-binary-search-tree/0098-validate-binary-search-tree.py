# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

def dfs(root: Optional[TreeNode], min_val = -sys.maxsize, max_val = sys.maxsize) -> bool:
    if root is None:
        return True
    
    if min_val >= root.val or root.val >= max_val:
        return False
    
    return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return dfs(root)