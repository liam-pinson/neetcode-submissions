class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        paren_map = { ")": "(", "}": "{", "]": "["}

        for c in s:
            if c not in paren_map:
                stack.append(c)
            else:
                if not stack or stack[-1] != paren_map[c]:
                    return False
                stack.pop()

        return stack == []