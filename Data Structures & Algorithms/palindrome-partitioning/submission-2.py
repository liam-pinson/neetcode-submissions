class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        subset = []

        def backtrack(i):

            if i >= len(s):
                res.append(subset[:])
                return
            
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    subset.append(s[i:j+1])
                    backtrack(j + 1)
                    subset.pop()
        
        backtrack(0)
        return res

    def isPalin(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True