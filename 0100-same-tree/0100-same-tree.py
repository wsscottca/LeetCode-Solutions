'''
Timestamps:
    Understand and Cases:
    Design and Verify:
    Code:
    
Understand and Cases:
    p = [1], q = [1]
    p = [1,2,3] q = [1,2]

Design and Verify:
    DFS compare elements
    
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
        
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)