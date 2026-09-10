class Solution:
    def numSquares(self, n: int) -> int:
        '''
        nums = []
        i = 1
        while i*i < n:
            nums.append(i*i)
            i+=1
        if n == 1:
            return 1
        memo = {}
        def dfs(i):
            if i == 0:
                return 0
            if i <0:
                return float('inf')
            if i in memo:
                return memo[i]
            memo[i] = float('inf')
            for num in nums:
                memo[i] = min(memo[i] , 1+dfs(i-num))
            return memo[i]
        return dfs(n)
        '''
        #tabulation bottom-up
        nums = []
        i = 1
        while i*i <= n:
            nums.append(i*i)
            i+=1
        if n == 1:
            return 1
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for num in nums:
                if i >= num:
                    dp[i] = min(dp[i] , 1 + dp[i-num])
        return dp[n]



        