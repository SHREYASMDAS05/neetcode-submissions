class Solution:
    def numDecodings(self, s: str) -> int:
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

        return dfs(0)
            