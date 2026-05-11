# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def rec(root, cur):
            print(root, cur)

            if not cur:
                return root
            
            root = rec(root, cur.next)
            # print(root.val, cur.val)
            if not root:
                return None

            temp = None
            if root == cur or root.next == cur:
                cur.next = None
            else:
                temp = root.next
                root.next = cur
                cur.next = temp

            return temp


        ans = rec(head, head.next)

        return