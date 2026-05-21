class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        n = len(nums)
        target = int(total / 2)
        memo = [[-1] * (target + 1) for _ in range(n)]
    
        def dfs(i, target):
            if i >= n:
                return target == 0
            if target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            
            memo[i][target] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return memo[i][target]
        
        return dfs(0, target)