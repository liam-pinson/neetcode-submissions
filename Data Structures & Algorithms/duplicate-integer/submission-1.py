class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}

        for num in nums:
            if dups.get(num, 0) == 1:
                return True
            dups[num] = 1

        return False