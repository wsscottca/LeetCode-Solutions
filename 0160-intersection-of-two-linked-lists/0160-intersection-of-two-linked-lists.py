# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA = headA
        pointerB = headB
        
        while pointerA or pointerB:
            if pointerA == pointerB:
                return pointerA
            
            if not pointerA:
                pointerA = headB
            else:
                pointerA = pointerA.next
            
            if not pointerB:
                pointerB = headA
            else:
                pointerB = pointerB.next
        
        return None
            