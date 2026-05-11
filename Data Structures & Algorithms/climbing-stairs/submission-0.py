class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [-1] * n
        def dfs(i):
            # base case
            if i >= n:
                return i == n
            print(i, cache[i], cache)
            # constraint
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        
        return dfs(0)
