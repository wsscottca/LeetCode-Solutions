'''
Timestamps:
    Cases: 1:33
    Design: 4:42
    Verify: 6:00
    Code:

Understand and Cases:
    root = None
    root = [1]
    
Design and Verify:
    BFS swap children

    q = deque()
    q.append(root)
    
    while q:
        node = q.popleft()
        
        if not node:
            continue
        
        temp = node.left
        node.left = node.right
        node.right = temp
        
        q.append(node.left)
        q.append(node.right)
    
    return root


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # queue for BFS
        q = deque()
        q.append(root)
        
        # while there are nodes
        while q:
            # pop our node
            node = q.popleft()
            
            # if there isn't a node just skip
            if not node:
                continue

            # otherwise swap the children
            temp = node.left
            node.left = node.right
            node.right = temp

            # and add the children to the queue
            q.append(node.left)
            q.append(node.right)
        
        # finally return the root
        return root