class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n , m = len(word1) , len(word2)
        dp = [[-1]*(m+1) for i in range(n+1)]
        def dfs(i , j):
            #base case
            if i<0:
                return j+1
            if j < 0:
                return i + 1
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i] == word2[j]:
                dp[i][j] =  dfs(i-1 , j-1)
            else:
                dp[i][j] =  min(1+ dfs(i, j-1),1+dfs(i-1 , j) , 1+ dfs(i-1 , j-1))
            return dp[i][j] 
        return dfs(n-1 , m-1)
