# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        current_diameter = 0
        
        # nested dfs so we don't need an instance or global variable or passing a tuple up
        def dfs(node: Optional[TreeNode]):
            nonlocal current_diameter
            if not node:
                return 0
            
            # store our subtree results so we can calculate based on them
            left = dfs(node.left)
            right = dfs(node.right)
            
            # if our calculated diameter is larger than our current_diameter set it
            if (left + right) > current_diameter:
                current_diameter = left + right
            
            return max(left, right) + 1
        
        # call nested function
        dfs(root)
        
        # return final diameter
        return current_diameter