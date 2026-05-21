class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            res = cost[i] + min(dfs(i + 1), dfs(i + 2))

            memo[i] = res
            return memo[i]
        
        return min(dfs(0), dfs(1))