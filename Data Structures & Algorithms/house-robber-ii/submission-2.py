class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        '''
        if n == 1:
            return nums[0]
        memo = {}
        def dfs(i , end):
            if i > end:
                return 0 
            if i in memo:
                return memo[i]
            rob = nums[i] + dfs(i+2 , end)
            skip = dfs(i +1 , end)

            memo[i] = max(rob , skip)
            return memo[i]
        skip_last = dfs(0,n-2)
        memo={} #reset memo
        skip_first = dfs(1,n-1)
        return max( skip_last , skip_first)
        '''
        #tabulatoin from bottom to top
        if n == 1:
            return nums[0]
        dp1 = [0] * (n+2)
        dp2 = [0] * (n+2)
        for i in range(n-1 , 0 , -1):
            dp1[i] = max(nums[i] + dp1[i+2] ,dp1[i+1] )
        for i in range(n-2 , -1 , -1):
            dp2[i] = max(nums[i] + dp2[i+2] ,dp2[i+1] )

        return max(dp1[1] , dp2[0])


        
