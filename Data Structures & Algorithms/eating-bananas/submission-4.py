class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / mid)
            
            if totalTime <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans