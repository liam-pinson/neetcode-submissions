class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []
        candidates.sort()

        def dfs(i, amount):
            if amount == target:
                res.append(subset[:])
                return
            if i >= len(candidates) or amount > target:
                return
            
            subset.append(candidates[i])
            dfs(i + 1, amount + candidates[i])
            subset.remove(candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, amount)

        dfs(0,0)
        return res