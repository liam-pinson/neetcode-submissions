class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest = float("-inf")
        curr_sum = 0

        for num in nums:
            if curr_sum + num < 0:
                curr_sum = 0
            else:
                curr_sum += num
                largest = max(largest, curr_sum)

        return largest if largest > float("-inf") else max(nums)