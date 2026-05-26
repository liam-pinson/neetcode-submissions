class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = float("-inf")

        for i in range(len(heights)):
            smallest = heights[i]

            # left
            l = r = i
            while l >= 0 and heights[l] >= smallest:
                l -= 1

            # right
            while r < len(heights) and heights[r] >= smallest:
                r += 1

            l += 1
            r -= 1
            maxArea = max(maxArea, smallest * (r - l + 1))
        
        return maxArea