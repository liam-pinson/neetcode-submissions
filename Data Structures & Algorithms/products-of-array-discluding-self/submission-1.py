class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)

        for i in range(len(nums)):
            arr = nums[:i] + nums[i+1:]
            product = 1
            for n in arr:
                product *= n
            output[i] *= product
        
        return output