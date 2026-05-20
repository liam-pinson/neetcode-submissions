class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res, subset = [], []

        def backtrack(opened: int, closed: int):
            if opened == closed == n:
                res.append("".join(subset[:]))
                return
            
            if opened < n:
                subset.append("(")
                backtrack(opened + 1, closed)
                subset.pop()
            if closed < opened:
                subset.append(")")
                backtrack(opened, closed + 1)
                subset.pop()

        backtrack(0, 0)
        return res