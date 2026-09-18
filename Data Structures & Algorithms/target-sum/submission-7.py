class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        memo = {}
        def dfs(i , cursum):
            if i == len(nums):
                return 1 if cursum == target else 0
            if (i , cursum) in memo:
                return memo[(i , cursum)]
            
            memo[(i,cursum)] = dfs(i+1 , cursum + nums[i]) + dfs(i+1 , cursum - nums[i])
            return memo[(i,cursum)]
        return dfs(0 ,0)
        '''
        n = len(nums) 
        total = sum(nums) 
        offset = total
        dp = [[0]*(2*total + 1) for i in range(n+1)]
        
        if abs(target) > total:
            return 0
        dp[n][target + offset] = 1
        for i in range(n-1 , -1 , -1):
            for cursums in range(-total , total + 1):
                if cursums + nums[i] <= total:
                    dp[i][cursums + offset] += dp[i+1][cursums + offset +   nums[i]]
                if cursums - nums[i] >= -total:
                    dp[i][cursums + offset] += dp[i+1][cursums - nums[i] + offset]
        return dp[0][offset]