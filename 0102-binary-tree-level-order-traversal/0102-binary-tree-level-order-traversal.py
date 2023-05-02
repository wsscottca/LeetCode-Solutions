from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        
        i = 0
        visited = set()
        to_visit = deque()
        to_visit.append((root, i))
        res = [[]]            
        
        while to_visit:
            curr = to_visit.popleft()
            curr_i = curr[1]
            curr = curr[0]

            if curr in visited:
                continue
            
            visited.add(curr)
            if curr_i > i:
                res.append([])
                i += 1
            res[i].append(curr.val)
            
            if curr.left and curr.left not in visited:
                to_visit.append((curr.left, i + 1))
            
            if curr.right and curr.right not in visited:
                to_visit.append((curr.right, i + 1))
        
        return res