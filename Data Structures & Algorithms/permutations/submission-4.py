class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            for num in nums:
                if num in subset:
                    continue
                subset.append(num)
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        return res