# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def _isSymmetric(root_a: Optional[TreeNode], root_b: Optional[TreeNode]) -> bool:
    if root_a is None and root_b is None:
        return True
    elif root_a is None or root_b is None:
        return False
    elif root_a.val != root_b.val:
        return False

    return _isSymmetric(root_a.left, root_b.right) and _isSymmetric(root_a.right, root_b.left)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        
        return _isSymmetric(root.left, root.right)