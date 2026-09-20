class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1]*(len(p)+1) for i in range(len(s)+1)]
        def dfs(i , j):
            if i >= len(s) and j >= len(p):
                return True
            if j>= len(p):
                return False
            if dp[i][j] != -1:
                return dp[i][j]
            match = i<len(s) and (s[i] == p[j] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                dp[i][j] = dfs(i,j+2) or (match and dfs(i+1 , j))#don't use and use
                return dp[i][j]
            if match:
                dp[i][j] = dfs(i+1 , j+1 )
                return dp[i][j]
            dp[i][j] = False
            return dp[i][j]
        return dfs(0 ,0)
