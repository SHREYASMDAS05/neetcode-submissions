class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n , m = len(s) , len(t)
        memo = {}
        def dfs(i , j):
            if j <0 :
                return 1
            if i< 0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)] 
            if s[i] == t[j]:
                #return dfs(i-1,j-1) + dfs(i-1 , j)
                memo[(i,j)] = dfs(i-1,j-1) + dfs(i-1 , j)
            else:
                #return dfs(i-1 ,j)
                memo[(i,j)]  = dfs(i-1 ,j)
            return memo[(i,j)] 
            
            
        return dfs(n-1 , m-1)