class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        subset = []
        num_arr = [i for i in range(1, n + 1)]

        def backtrack(i):
            if len(subset) == k:
                res.append(subset[:])
                return
            if i >= n:
                return
            
            subset.append(num_arr[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res