class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row  , col = len(matrix) , len(matrix[0])
        l , r = 0 , row * col -1
        while l <= r:
            m = (l + r) // 2
            i , j = m // col , m % col

            if matrix[i][j] == target:
                return True

            elif matrix[i][j] > target:
                r = m - 1

            else:
                l = m + 1
        return False

