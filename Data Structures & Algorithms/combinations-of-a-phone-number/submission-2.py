class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        subset = []

        def backtrack(i):
            if len(subset) == len(digits):
                res.append("".join(subset[:]))
                return
            if i >= len(digits):
                return
            
            for c in num_map[digits[i]]:
                subset.append(c)
                backtrack(i + 1)
                subset.pop()
            return
        
        backtrack(0)
        print(res)
        return res