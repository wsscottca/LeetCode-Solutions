# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def _maxDepth(root: Optional[TreeNode], depth: int) -> int:
    if not root:
        return depth - 1
    
    left = _maxDepth(root.left, depth + 1)
    right = _maxDepth(root.right, depth + 1)
    
    return max(left, right)
        

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return _maxDepth(root, 1)

        