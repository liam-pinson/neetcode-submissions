class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def backtrack(i, amount):
            if i >= len(nums) or amount > target:
                return
                
            if amount == target:
                res.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i, amount + nums[i])
            subset.pop()
            backtrack(i + 1, amount)

        backtrack(0, 0)
        return res