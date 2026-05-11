# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def add(self, v1, v2, carry = 0):
        if not v1 and not v2 and carry == 0:
            return None

        n1 = v1.val if v1 else 0
        n2 = v2.val if v2 else 0

        carry, val = divmod(n1 + n2 + carry, 10)

        newNode = self.add(
            v1.next if v1 else None,
            v2.next if v2 else None,
            carry
        )

        return ListNode(val, newNode)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1, l2, 0)
        