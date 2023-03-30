# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (not head or head.next is None):
            return False
        fast = head.next
        slow = head

        while True:
            if (fast == slow):
                return True
            
            for i in range(2):
                if (fast.next is None):
                    return False

                if i == 0:
                    fast = fast.next
                    slow = slow.next
                else:
                    fast = fast.next
            
            
        