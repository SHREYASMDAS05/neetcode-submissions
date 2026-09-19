class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows , cols = len(matrix) , len(matrix[0])
        dp = {} #(r,c) val of LIP
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r , c , prev_val):
            if r<0 or r== rows or c<0 or c== cols or prev_val >= matrix[r][c]:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res = 0 
            for dr , dc in directions:
                nr , nc = r + dr , c + dc
                res = max(res , 1+ dfs(nr,nc , matrix[r][c]))

            dp[(r,c)] = res
            return res
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,-1)
        return max(dp.values())
