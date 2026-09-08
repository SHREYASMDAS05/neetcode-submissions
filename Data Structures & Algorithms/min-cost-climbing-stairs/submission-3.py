class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        n = len(cost)
        dp = [0] * (n + 2)
        for i in range(n-1 , -1 , -1):
            dp[i] = cost[i] + min(dp[i+1] , dp[i+2])

        return min(dp[0] , dp[1])
        '''
        n = len(cost)
        next1 = 0 #dp[i+1]
        next2  = 0 #dp[i+2]
        for i in range(n-1 , -1 , -1):
            curr = cost[i] + min(next1 , next2)
            next2 = next1
            next1 = curr

        return min(next1 , next2)