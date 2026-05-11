class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i, amount):
            if i >= len(nums):
                return 
            if amount == target:
                res.append(subset[:])
                return
            
            if amount > target:
                return
            
            subset.append(nums[i])
            dfs(i, amount + nums[i])
            subset.remove(nums[i])
            dfs(i + 1, amount)

        dfs(0, 0)

        return res