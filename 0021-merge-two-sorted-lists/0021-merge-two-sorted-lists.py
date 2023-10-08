'''
Timestamps:
    Tests: 1:50
    Verify: 9:32
    Code:
    
Tests:
    list1 = [1,1,1]
    list2 = [1,1]
    
    list1 = [1,2,3,4,5]
    list2 = []
    
Design and Verify:
    
    head = ListNode()
    node = head
    while list1 or list2:
        if not list1:
            node.next = list2
            return head.next
        if not list2:
            node.next = list1
            return head.next
        
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
            
        node = node.next
        
    return head
        
    
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        head = ListNode()
        node = head
        while list1 or list2:
            if not list1:
                node.next = list2
                return head.next
            if not list2:
                node.next = list1
                return head.next

            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next

        return head