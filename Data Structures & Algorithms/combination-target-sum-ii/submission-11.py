class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, subset = [], []
        candidates.sort()

        def backtrack(i, amount):
            if amount == target:
                res.append(subset[:])
                return
            if i >= len(candidates) or amount > target:
                return
            
            subset.append(candidates[i])
            backtrack(i + 1, amount + candidates[i])
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            backtrack(i + 1, amount)

        backtrack(0,0)
        return res