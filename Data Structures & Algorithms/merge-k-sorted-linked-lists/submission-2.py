# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        vals = []

        for node in lists: 
            curr = node
            while curr:
                vals.append(curr.val)
                curr = curr.next
        
        vals.sort()
        dummy = curr = ListNode(0)
        for val in vals:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next