class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        memo = {}
        def dfs(num):
            if num == 1:
                return 1
            res = 0 
            if num in memo:
                return memo[num]
            for i in range(1,num//2 + 1):
                val = i * dfs(num - i)
                val2 = i * (num -i)
                res = max(val , res , val2)
            memo[num] = res
            return memo[num]
        return dfs(n)
        '''
        dp = [0] * (n + 1)
        dp[1] = 1
        for num in range(2 , n+1):
            for i in range(1, num):
                val1 = i * (num-i)
                val2 = i * dp[num - i]
                dp[num] = max(dp[num], val2 , val1)

        return dp[n]

