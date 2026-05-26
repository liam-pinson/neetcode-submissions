class Solution:
    def isValid(self, s: str) -> bool:
        
        paren_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c not in paren_map:
                stack.append(c)
            elif stack and stack[-1] == paren_map[c]:
                stack.pop()
            else:
                return False
        
        return stack == []