class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []

        for i, num in enumerate(nums):
            # print(i, num, queue, res)
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            
            # print(i, k , queue)
            if queue and queue[0] <= i - k:
                queue.popleft()

            if queue and i >= k - 1:
                res.append(nums[queue[0]])

            # print()

        return res