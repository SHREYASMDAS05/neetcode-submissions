class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1 
        if n== 2:
            return 2
        if n== 0:
            return 1
        dp =[-1] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for curr in range(3 , n+1):
            dp[curr] = dp[curr-1] + dp[curr-2]
            
        return dp[n]