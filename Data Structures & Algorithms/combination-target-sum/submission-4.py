class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if total > target or i >= len(nums):
                return
            
            cur.append(nums[i])

            # include
            dfs(i, cur, total + nums[i])
            cur.pop()

            # exclude
            dfs(i + 1, cur, total)


        
        dfs(0, [], 0)
        return res