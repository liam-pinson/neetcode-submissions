class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = float("-inf")
        n = len(heights)

        for i in range(n):
            height = heights[i]

            l = r = i
            # left
            while l >= 0 and heights[l] >= height:
                l -= 1

            # right
            while r < n and heights[r] >= height:
                r += 1
            
            l += 1
            r -= 1
            maxArea = max(maxArea, height * (r - l + 1))

        return maxArea