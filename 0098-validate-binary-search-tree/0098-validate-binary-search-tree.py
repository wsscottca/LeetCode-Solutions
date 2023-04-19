# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def _validBST(root: Optional[TreeNode], minVal, maxVal) -> bool:
        if root is None:
            return True
        
        if not (root.val > minVal and root.val < maxVal):
            return False
        elif root.left is not None and root.left.val >= root.val:
            return False
        elif root.right is not None and root.right.val <= root.val:
            return False

        return _validBST(root.left, minVal, root.val) and _validBST(root.right, root.val, maxVal)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return _validBST(root, float(-inf), float(inf))

    