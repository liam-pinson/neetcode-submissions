"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodes = {}

        def rec(root):
            if not root:
                return None
            
            if root in nodes:
                return nodes[root]
            
            copy = Node(root.val)
            nodes[root] = copy
            copy.next = rec(root.next)
            copy.random = nodes.get(root.random)

            return copy
        
        return rec(head)