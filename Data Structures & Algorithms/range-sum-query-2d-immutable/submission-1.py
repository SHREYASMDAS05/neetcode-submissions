class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        rows , cols = len(matrix) , len(matrix[0])
        self.summat = [[0]* (cols +1) for i in range(rows +1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                self.summat[r+1][c+1] = prefix + self.summat[r][c+1]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 , r2, c1 , c2 = row1 + 1 , row2 + 1 , col1 + 1 , col2 + 1
        bottom_right = self.summat[r2][c2]
        top_right = self.summat[r1-1][c2]
        bottom_left = self.summat[r2][c1 - 1]
        top_left = self.summat[r1-1][c1-1]

        return bottom_right - top_right - bottom_left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)