# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        front = head
        back = head
        
        for i in range(n + 1):
            if not front:
                return back.next
            front = front.next
        
        while front:
            front = front.next
            back = back.next
        
        front = back.next.next
        back.next = front
        
        return head