class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)

        for i in range(n):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                j += 1
            count = 0 if j >= n else j - i
            res.append(count)

        return res


