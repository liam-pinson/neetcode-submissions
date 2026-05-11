class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm, nums, pick):
        # base case
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return

        for i in range(len(nums)):
            if not pick[i]:

                # INCLUDE, true as to not pick the same number again
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)

                # REPLACE, NOT EXCLUDE
                perm.pop()
                pick[i] = False
            
