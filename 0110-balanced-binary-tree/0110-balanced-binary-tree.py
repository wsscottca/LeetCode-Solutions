'''
Timestamps:
    Cases: 1:51
    Design: 5:58
    Verify: 7:05
    Code: 9:51
    
Understand and Cases:
    root = [1,null,1,null,null,1,null] - False +2
    root = [1,1,1]

Design and Verify:
    
    
    def height(root):
        if root is None:
            return 0
        
        return max(root.left, root.right) + 1
        
    left = height(root.left)
    right = height(root.right)
    
    if ((abs(left-right)) <= 1) and isBalanced(root.left) and isBalanced(root.right):
        return True
        
    return False

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # nested function to get the height of the subtrees
        def _height(root):
            # if there is no root return 0
            if root is None:
                return 0
            
            # otherwise return the taller subtree + 1 for our current node
            return max(_height(root.left), _height(root.right)) + 1

        # get the height of the left and right subtree
        left = _height(root.left)
        right = _height(root.right)
        
        # check that the differences in the height is <= 1 and that
        # all subtrees are balanced as well
        if ((abs(left-right)) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        # if we get here they are not balanced at some point
        return False