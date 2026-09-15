class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:      
        '''
        brute force
        def gene_subseq(s):
            res = []
            def subseq(i,curr):
                if i == len(s):
                    res.append(curr.copy())
                    return
                curr.append(s[i])
                subseq(i +1 , curr)
                curr.pop()
                subseq(i+1 , curr)
            subseq(0,[])
            return res
        l1 = gene_subseq(text1 )
        l2 = gene_subseq(text2 )
        maxi = 0 
        for i in l1:
            for j in l2:
                if i == j and len(i) > maxi:
                    maxi = len(i)
        return maxi 
        
        memo ={}
        def dfs(idx1 , idx2):
            if idx1< 0 or idx2< 0 :
                return 0 
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]
            if text1[idx1] == text2[idx2]:
                memo[(idx1,idx2)] = 1 + dfs(idx1 -1 , idx2 -1 )
                return 1 + dfs(idx1 -1 , idx2 -1 )
            else:
                memo[(idx1,idx2)] = 0 + max(dfs(idx1-1,idx2) , dfs(idx1,idx2-1))
                return 0 + max(dfs(idx1-1,idx2) , dfs(idx1,idx2-1))

        return dfs(len(text1)-1,len(text2)-1)
        '''
        #tbultion bottom up 
        m , n = len(text1) , len(text2)
        dp = [[0] * (n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

        return dp[m][n]


