import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if not piles:
            return -1


        low, high = 1, max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            time = sum(math.ceil(p / mid) for p in piles)

            if time <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans