class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        sol = float("-inf")

        i, j = 0, len(heights) - 1
        while i < j:
            calc = (j - i) * min(heights[i], heights[j])
            sol = max(calc, sol)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return sol