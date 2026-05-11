# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def rec(self, root, cur):
        if not cur:
            return root
        
        root = self.rec(root, cur.next)
        if not root:
            return None
        
        temp = None
        if root == cur or root.next == cur:
            cur.next = None
            return None
        else:
            temp = root.next
            root.next = cur
            cur.next = temp

        return temp

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        self.rec(head, head.next)