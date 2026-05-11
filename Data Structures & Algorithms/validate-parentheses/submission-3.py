class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        c_end_map = { ')': '(', '}': '{', ']': '[' }

        for c in s:
            print(c)
            print(stack)
            if c in c_end_map:
                if stack and stack[-1] == c_end_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return stack == []