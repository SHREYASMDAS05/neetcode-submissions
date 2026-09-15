class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m , n = len(obstacleGrid) , len(obstacleGrid[0])
        '''
        memo = {}
        if obstacleGrid[0][0] == 1:
            return 0
        def dfs(i , j):
            if i == 0 and j ==0 :
                return 1
            if i < 0 or j < 0:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0 
            if (i,j) in memo:
                return memo[(i,j)]
            up = dfs(i-1 , j)
            left = dfs(i ,j-1)
            memo[(i,j)] = up + left
            return up + left
        return dfs(m-1,n-1)
        '''
        #tabulation adding bottom-up
        '''
        dp = [[-1] * n for i in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0 
        else:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 :
                    continue
                up = dp[i-1][j] if i>0 else 0
                left = dp[i][j-1] if j > 0 else 0
                dp[i][j] = (up + left) if obstacleGrid[i][j] == 0 else 0
        return dp[m-1][n-1]
        '''
        #tabulation with space optimization
        prev = [0] * n
        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0 :
                    if obstacleGrid[i][j] == 1:
                        return 0
                    curr[j] = 1
                    continue
                up = prev[j] if i > 0 else 0
                left = curr[j-1] if j > 0 else 0
                curr[j] = up + left if obstacleGrid[i][j] == 0 else 0
            prev = curr.copy()

        return prev[n-1]


        