class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        memo = {}
        def dfs(i , j):
            
            if i == 0 and j == 0 :
                return grid[i][j]
            if i < 0 or j  < 0 :
                return float('inf')
            if (i , j) in memo:
                return memo[(i , j)]
            up = dfs(i-1,j)
            left = dfs(i , j-1)
            memo[(i,j)] = grid[i][j] + min(left , up)
            return grid[i][j] + min(left , up)
        return dfs(m-1 , n-1)
