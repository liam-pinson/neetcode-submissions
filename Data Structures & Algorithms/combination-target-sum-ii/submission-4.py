class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def combo(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if total > target or i >= len(candidates):
                return 
            
            cur.append(candidates[i])
            # include
            combo(i + 1, cur, total + candidates[i])
            cur.pop()

            # make sure no duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # exclude
            combo(i + 1, cur, total)


        combo(0, [], 0)
        return res