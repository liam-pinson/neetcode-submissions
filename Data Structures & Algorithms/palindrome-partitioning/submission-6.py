class Solution:
    def isPalin(self, s: str, i: int, j: int):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(s):
                res.append(subset[:])
                return
            
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    subset.append(s[i:j + 1])
                    backtrack(j + 1)
                    subset.pop()
            
        backtrack(0)
        return res