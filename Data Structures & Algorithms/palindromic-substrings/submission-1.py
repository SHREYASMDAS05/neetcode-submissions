class Solution:
    def countSubstrings(self, s: str) -> int:
        '''n = len(s)
        def dfs(l , r):
            if l < 0 or r >= n or s[l] != s[r]:
                return 0 
            return 1 + dfs(l-1 , r+1)

        res = 0 
        for i in range(n):
            res += dfs(i , i ) # for odd length
            res += dfs(i , i +1) # for even length 

        return res
        '''
        #manacher's algorithm
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        p = [0] * n
        centre = 0 
        right = 0
        count = 0 
        for i in range( 1 , n-1):
            #compute the mirror 
            mirror = 2*centre - i
            #check if i can use it and use it 
            if i < right:
                p[i] = min(right - i , p[i])

            #go till next 
            while t[i+p[i]+1] == t[i-p[i] -1]:
                p[i] +=1
        for i in range(n):
            count += (p[i] + 1)//2

        return count

            