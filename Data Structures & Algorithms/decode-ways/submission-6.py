class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        n = len(s)
        memo = [-1] * (n+1)
        if int(s[0]) == 0:
            return 0
        def dfs(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if memo[i] != -1 :
                return memo[i]
            ways = dfs(i+1)
            if i < n and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i+2)
            memo[i] = ways
            return memo[i]

        return dfs(0)'''

        #tabulation from bottom to up 
        n = len(s)
        '''dp = [-1] * (n+2)
        dp[n] =1
        for i in range(n-1 , -1 , -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            dp[i] = dp[i +1]
            if i <n and 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]

        return dp[0]
        '''
        if int(s[0]) == 0:
            return 0
        prev1 = 1
        prev2 = 0
        for i in range(n-1 , -1 , -1):
            if s[i] == '0':
                curr = 0
            else:    
                curr = prev1
                if i+1 <n and 10 <= int(s[i:i+2]) <= 26:
                    curr += prev2
            prev2 = prev1 
            prev1 = curr
        return prev1




            