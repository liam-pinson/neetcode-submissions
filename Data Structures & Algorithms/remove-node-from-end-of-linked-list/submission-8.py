# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def rec(root, n):
            if not root:
                return
            
            print(root.val)

            root.next = rec(root.next, n)

            n[0] -= 1
            if n[0] == 0:
                return root.next
            return root
        
        return rec(head, [n])