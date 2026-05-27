class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                resTemp, resIdx = stack.pop()
                res[resIdx] = i - resIdx
            stack.append((temp, i))
        
        return res