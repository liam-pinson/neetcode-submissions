class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            if i >= len(nums):
                return
            
            for i in range(len(nums)):
                if nums[i] not in subset:
                    subset.append(nums[i])
                    backtrack(i)
                    subset.remove(nums[i])

        backtrack(0)
        return res