class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            for j in range(i , len(s)):
                if s[i:j+1] in wordDict:
                    if dfs(j+1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return dfs(0)
        '''
        n = len(s) 
        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n-1 , -1 , -1):
            for j in range(i,n):
                if s[i:j+1] in wordDict and dp[j+1]:
                    dp[i] = True
                    break
        return dp[0]
