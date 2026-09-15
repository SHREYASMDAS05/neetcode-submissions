class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        '''
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
        '''
        '''
        dp = [[-1] * n for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j ==0 :
                    continue
                up = dp[i-1][j] if i > 0 else float('inf')
                left = dp[i][j-1] if j > 0 else float('inf')
                dp[i][j] = grid[i][j] + min(up , left)

        return dp[m-1][n-1]
        '''
        prev = [0] * n
        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = grid[0][0]
                    continue
                left = curr[j-1] if j > 0 else float('inf')
                up = prev[j] if i > 0 else float('inf')
                curr[j] = grid[i][j] + min(left , up) 
            prev = curr.copy()
        return prev[n-1]