class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m , n = len(obstacleGrid) , len(obstacleGrid[0])
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

        