class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalsum = sum(stones)
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

