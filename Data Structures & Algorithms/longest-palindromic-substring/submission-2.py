class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''n = len(s)
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
        '''
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        p = [0] *n
        max_len = 0 
        max_centre = 0 
        centre = 0 
        right = 0 
        for i in range(1 , n-1):
            #find mirror of the point
            mirror = centre *2 - i
            #reuse the exisiting p[mirror]
            if i < right:
                p[i] = min(right - i , p[mirror])
            #go on calculting next
            while t[i + p[i] + 1] == t[i-p[i] -1]:
                p[i] +=1 
            #update the righmost 
            if i + p[i] > right:
                right = i + p[i]
                centre = i
            #if it's the max length
            if p[i] > max_len:
                max_len = p[i]
                max_centre = i

        start = (max_centre - max_len)//2
        return s[start : start + max_len]

            
