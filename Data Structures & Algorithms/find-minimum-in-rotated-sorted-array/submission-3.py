class Solution:
    def findMin(self, nums: List[int]) -> int:

        if not nums:
            return -1
        
        i, j = 0, len(nums) - 1
        sol = nums[i]

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] < sol:
                sol = nums[mid]
                j = mid - 1
            else:
                i = mid + 1

        return sol