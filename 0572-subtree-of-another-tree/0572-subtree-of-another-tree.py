'''
Timestamps:
    Understand and Cases: 2:00
    Design and Verify: 19:32
    Code:


Understand and Cases:
    root = [1] subRoot = [1]
    root = [1] subRoot = []
    
Design and Verify:
    Questions:
        Does it compare based on value or on object?
        If one is none does that default to T or F?
    
    DFS
    
    Find the root of the subtree
    Check if all branches are the same
    
    stack
    stack.append(root)
    
    while stack:
        node = stack.pop()
        if node.val == subRoot.val:
            if dfs_match(node, subRoot):
                return True
        
        stack.append(node.left, node.right)
    
    return false
    
    dfs_match(root, subRoot)
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        
        left = dfs_match(root.left, subRoot.left)
        right = dfs_match(root.right, subRoot.right)
        
        return left and right
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs_match(root: TreeNode, subRoot: TreeNode):
            if not root and not subRoot:
                return True
            elif not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False

            left = dfs_match(root.left, subRoot.left)
            right = dfs_match(root.right, subRoot.right)

            return left and right
        
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val == subRoot.val:
                if dfs_match(node, subRoot):
                    return True

            stack.append(node.left)
            stack.append(node.right)

        return False