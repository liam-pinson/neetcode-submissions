# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def rec(root, curr):
            # base case
            if not curr:
                return root

            # traverse to the end
            root = rec(root, curr.next)
            
            if not root:
                return None
            
            temp = None
            if root == curr or root.next == curr:
                curr.next = None
            else:
                temp = root.next
                root.next = curr
                curr.next = temp
            
            return temp
        
        ans = rec(head, head.next)

        return