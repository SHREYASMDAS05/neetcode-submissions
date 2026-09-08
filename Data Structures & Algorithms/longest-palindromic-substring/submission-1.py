class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best_l = 0
        best_r = 0 
        def dfs(l , r):
            if l <0 or r >= n or s[l] != s[r]:
                return 
            nonlocal best_l , best_r
            if r-l > best_r - best_l:
                best_r = r
                best_l = l

            dfs(l-1 , r+1)

        for i in range(n):
            dfs(i , i) # for odd length
            dfs(i , i+1) #for the even length 

        return s[best_l : best_r+1]
