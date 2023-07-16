import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        pointer = head
        min_heap = []
        
        if not lists:
            return None
        
        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, id(node), node))
            
        while min_heap:
            _, _, node = heapq.heappop(min_heap)
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, id(node.next), node.next))
            
            pointer.next  = node
            pointer = pointer.next
            
        return head.next
        
        