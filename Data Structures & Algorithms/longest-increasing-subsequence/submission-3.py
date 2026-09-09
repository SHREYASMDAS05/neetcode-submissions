class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        memo = {}
        def dfs(i , prev):
            if i == len(nums):
                return 0 
            if (i , prev) in memo:
                return memo[(i,prev)]
            skip = dfs(i+1 , prev)
            take = 0 
            if nums[i] > nums[prev] or prev == -1:
                take = 1 + dfs(i+1 , i)
            memo[(i , prev)] = max(skip , take)
            return memo[(i , prev)]
        return dfs(0 , -1)
        '''
        #tabulation bottom to up 
        n = len(nums)
        dp = [[0] *(n+1) for i in range(n+1)]
        for i in range(n-1 , -1 , -1):
            for prev in range(i-1 , -2 ,-1):
                #skip 
                skip = dp[i+1][prev+1]
                #take
                take = 0
                if nums[i] > nums[prev] or prev == -1:
                    take = 1 + dp[i+1][i+1]
                dp[i][prev+1] = max(skip , take)

        return dp[0][0]
        