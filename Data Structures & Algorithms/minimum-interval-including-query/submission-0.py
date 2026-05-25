class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = []

        for query in queries:
            length = float("inf")
            for interval in intervals:
                if interval[0] <= query <= interval[1]:
                    length = min(length, interval[1] - interval[0] + 1)
            ans = -1 if length >= float("inf") else length
            res.append(ans)

        return res