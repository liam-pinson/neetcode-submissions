class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement = {}

        for i, val in enumerate(nums):
            if target - val in complement:
                return [min(i, complement[target - val]), max(i, complement[target - val]) ]
            complement[val] = i