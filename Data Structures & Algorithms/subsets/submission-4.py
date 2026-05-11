class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])

            # INCLUDE
            dfs(i + 1)
            subset.pop()

            # EXCUDE
            dfs(i + 1)
        
        dfs(0)
        return res
        