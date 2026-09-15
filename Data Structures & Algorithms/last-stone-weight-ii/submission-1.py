class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalsum = sum(stones)
        '''
        memo = {}
        def dfs(i , total):
            if i == len(stones):
                return abs(total-(totalsum - total))
            #min of skipping and notskipping 
            if (i , total) in memo:
                return memo[(i , total)]
            memo[(i , total)] = min(dfs(i+1 , total) , dfs(i + 1 , total + stones[i]))
            return min(dfs(i+1 , total) , dfs(i + 1 , total + stones[i]))
        return dfs(0 , 0)
        '''
        target = totalsum // 2
        dp = [[False] * (target + 1) for i in range(len(stones) +1 )]
        for i in range(len(stones) + 1):
            dp[i][0] = True #can get sum 0 

        for i in range(1 ,len(stones) + 1):
            for j in range(1 , target + 1):
                #not taking 
                dp[i][j] = dp[i-1][j]
                #by taking
                if stones[i-1] <= j:
                    dp[i][j] = dp[i][j] or dp[i-1][j - stones[i -1]]    
        best = 0
        for i in range(target , -1 , -1):
            if dp[len(stones)][i] :
                best = i
                break
        return totalsum - 2*best

