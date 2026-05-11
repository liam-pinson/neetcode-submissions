class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = float("-inf")
        i, j = 0, len(heights) - 1

        while i < j:
            calc = (j - i) * min(heights[i], heights[j])
            res = max(res, calc)
            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
        
        return res