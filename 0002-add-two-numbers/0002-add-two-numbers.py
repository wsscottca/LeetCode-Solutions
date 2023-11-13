'''
Timestamps:
    Cases: 2:30
    Verify:
    Code:
    
Understand and Cases:
    l1 = [9] l2 = [1]
    l1 = [] l2 = []
    
Design and Verify:
    if not l1 and not l2:
        return None

    carry = 0
    head = ListNode()
    node = head
    
    while l1 or l2:
        if not l1:
            node.next = l2
            return head.next
        elif not l2:
            node.next = l1
            return head.next
            
        val = l1.val + l2.val + carry
        carry = 0
        
        if val > 9:
            carry = 1
            
        node.next = ListNode(val % 10)
        node = node.next
    
    if carry == 1:
        node.next = ListNode(1)
    
    return head.next
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry for maths
        carry = 0
        
        # dummy head for return
        head = ListNode()
        
        #pointer node
        node = head
        
        # while we have values to parse
        while l1 or l2:            
            # calculate our current value (account for our carry)
            if l1 and l2:
                val = l1.val + l2.val + carry
                
                # iterate our pointers
                l1 = l1.next
                l2 = l2.next
            
            # if there is only one calculate our value only using it
            elif l1:
                val = l1.val + carry
                l1 = l1.next
            
            else:
                val = l2.val + carry
                l2 = l2.next
            
            # set carry for next pass
            carry = 0
            if val > 9:
                carry = 1
            
            # add our ones place value to our ans
            node.next = ListNode(val % 10)
            node = node.next
            
            
        
        # if theres a left over carry, add it to the front
        if carry == 1:
            node.next = ListNode(1)
        
        return head.next