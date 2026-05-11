class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False
        
        i, j = 0, (len(matrix) * len(matrix[0])) - 1
        row_l = len(matrix[0])

        while i <= j:
            mid = (i + j) // 2
            
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            
            num = matrix[row][col]

            if num == target:
                return True
            elif num > target:
                j = mid - 1
            else:
                i = mid + 1

        return False
