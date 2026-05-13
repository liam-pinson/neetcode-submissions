"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        memo = {}
        
        def dfs(root):
            if not root:
                return None
            if root in memo:
                return memo[root]
            
            copy = Node(root.val)
            memo[root] = copy
            
            for nei in root.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node else None