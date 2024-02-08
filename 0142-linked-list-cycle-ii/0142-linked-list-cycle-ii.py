'''
Timestamps:
    Cases: 1:20
    Design: 3:00
    Verify: 5:13
    Code:
    
Understand and Cases:
    head = [1,2,3] pos = [-1]
    head = []

Design and Verify:
    Tortoise and hare
    
    # set our pointers
    slow = head
    fast = head
    
    # while they're not at the same point keep moving
    while slow and fast:
        slow = slow.next
        fast = fast.next.next
        
        # once they hit each other move slow to the head and
        # slowly increment both, once they hit again we have the start
        # so return it
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            
            return slow
    
    # if slow or fast = none there is no cycle
    return None

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # set our pointers
        slow = head
        fast = head

        # while they're not at the same point keep moving
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # once they hit each other move slow to the head and
            # slowly increment both, once they hit again we have the start
            # so return it
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        # if slow or fast = none there is no cycle
        return None