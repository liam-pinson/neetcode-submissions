class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map_ = {}

        for i, val in enumerate(nums):
            comp = target - val
            if comp in map_:
                return [min(i, map_[comp]), max(i, map_[comp])]
            map_[val] = i

        return 