class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for i in range(n)]
        def isvalid(r ,c):
            #to check in the col
            for i in range(r):
                if board[i][c] == 'Q':
                    return False
            #to check in the upper right diagonal 
            i , j = r -1 , c+1
            while i >=0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j+=1

            #to check in the upper left diagonal 
            i , j = r - 1 , c -1 
            while i >=0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j-=1
            return True

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return 
            for c in range(n):
                if isvalid(r,c):
                    board[r][c] = 'Q'
                    backtrack(r+1)
                    board[r][c] = '.'

        backtrack(0)
        return res


