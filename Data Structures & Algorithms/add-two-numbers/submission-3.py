# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def add(self, val1, val2, carry):

        if not val1 and not val2 and carry == 0:
            return None
        elif not val1 and not val2 and carry > 0:
            return ListNode(carry)
        elif val1 and not val2:
            r, q = divmod(val1.val + carry, 10)
            return ListNode(q, self.add(val1.next, None, r))
        elif val2 and not val1:
            r, q = divmod(val2.val + carry, 10)
            return ListNode(q, self.add(val2.next, None, r))

        print(val1.val, val2.val)

        r, q = divmod(val1.val + val2.val + carry, 10)
        print(r, q)
        node = ListNode(q, None)
        print(node.val)
        node.next = self.add(
            val1.next if val1.next else None, 
            val2.next if val2.next else None,
            r)

        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ans = self.add(l1, l2, 0)

        return ans