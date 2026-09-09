class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def dfs(l , r):
            if l < 0 or r >= n or s[l] != s[r]:
                return 0 
            return 1 + dfs(l-1 , r+1)

        res = 0 
        for i in range(n):
            res += dfs(i , i ) # for odd length
            res += dfs(i , i +1) # for even length 

        return res