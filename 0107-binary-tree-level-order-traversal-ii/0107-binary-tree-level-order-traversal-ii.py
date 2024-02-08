'''
Timestamps:
    Cases: 1:50
    Design: 12:30
    Verify: 15:52
    Code:
    
Understand and Cases:
    root = [1,2,3]
    root = [1,2,null,3,null,null,null]

Design and Verify:
    BFS, add each level to array reversed
    
    
    [[3], [9,20], [15,7]]
    q []
    nq []
    
    res = []    
    
    def bfs(q):
        res.append(q)
        new_q = deque()
        while q:
            node = q.pop()
            
            if node.left:
                new_q.append(node.left)
            
            if node.right:
                new_q.append(node.right)
        
        if new_q:
            bfs(new_q)
    
    q = deque()
    deque.append(node)
    bfs(q)
    return reversed(res)
            

'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # to store our result
        res = []    
    
        # helper bfs to track levels
        def bfs(q):
            # each start of our helper function
            # the current q holds a level so add it to the result
            arr = []
            for node in q:
                arr.append(node.val)
            res.append(arr)
            new_q = deque()
            
            # perform normal bfs, adding children to the new_q
            while q:
                node = q.popleft()
                
                if node.left:
                    new_q.append(node.left)

                if node.right:
                    new_q.append(node.right)

            # if there are items in our new q we need to continue our bfs
            if new_q:
                bfs(new_q)
        
        if root:
            # create initial q and add root
            q = deque()
            q.append(root)

            # perform our bfs
            bfs(q)
        
        # return the reversed of our result so it is bottom up not top down
        return reversed(res)