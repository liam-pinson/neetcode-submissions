class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # find mid first
        i, j = 0, len(nums) - 1
        pivot = i
        while i <= j:
            mid = (i + j) // 2

            if nums[mid] < nums[pivot]:
                pivot = mid
                j = mid - 1
            else:
                i = mid + 1

        def binary_search(left, right):

            i, j = left, right
            while i <= j:
                mid = (i + j) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1

            return -1

        check_left = binary_search(0, pivot - 1)

        if check_left != -1:
            return check_left
        return binary_search(pivot, len(nums) - 1)