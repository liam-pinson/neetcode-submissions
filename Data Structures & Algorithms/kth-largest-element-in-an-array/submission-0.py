class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums, self.k = nums, k
        self.nums = [-n for n in self.nums]
        heapq.heapify(self.nums)

        print(self.nums)

        while self.k > 1:
            heapq.heappop(self.nums)
            self.k -= 1

        return -heapq.heappop(self.nums)
