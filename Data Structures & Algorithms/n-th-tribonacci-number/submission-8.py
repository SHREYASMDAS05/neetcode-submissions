class Solution:
    def tribonacci(self, n: int) -> int:
        
        #memoization
        '''def dfs(n):
            if n==0:
                return 0 
            if n ==1 or n==2:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = dfs(n-1) + dfs(n-2) + dfs(n-3)

            return dp[n]

        return dfs(n)
        '''
        #tabulation
        '''
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3 , n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]
        '''
        #tabulation space optimization
        if n==0:
            return 0 
        if n ==1 or n==2:
            return 1
        prev1 = 1
        prev2 = 1
        prev3 = 0
        for i in range(3 , n+1):
            curr = prev1 + prev2 + prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = curr
        return prev1