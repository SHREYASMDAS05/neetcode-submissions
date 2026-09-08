class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        '''
        dp = [-1] * (n+1)
        def dfs(i):
            if i >= n:
                return 0 
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(nums[i] + dfs(i+2) ,dfs(i+1))

            return dp[i]

        return dfs(0)
        '''
        #tabulation
        '''dp = [0] * (n+2)
        dp[n] , dp[n+1] = 0 , 0 
        for i in range(n-1,-1 ,-1):
            dp[i] = max(nums[i] + dp[i+2] , dp[i+1])

        return dp[0]
        '''
        #tabulation with space optimization
        prev1 = 0 
        prev2 = 0 
        for i in range(n-1 , -1 , -1):
            curr = max(nums[i] + prev2 , prev1)
            prev2 = prev1
            prev1 = curr

        return prev1
