class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        '''
        memo = {}
        def dfs(i , prev_min , prev_max):
            if i ==n:
                return prev_max
            prev_min = prev_min * nums[i]
            prev_max = prev_max * nums[i]

            curr_max = max(nums[i] , prev_max , prev_min)
            curr_min = min(nums[i] , prev_max , prev_min)
            
            return max(curr_max ,dfs(i+1 , curr_min , curr_max))

        return dfs(1 , nums[0] , nums[0])
        '''
        #memoization doesn't chnge much 
        #we'll go for tabulation 
        '''
        dp = [[0,0] for i in range(n)]
        dp[0][0] , dp[0][1] = nums[0] , nums[0]
        ans = nums[0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] * nums[i]
            dp[i][1] = dp[i-1][1] * nums[i]
            curr_min = min(nums[i] , dp[i][0] , dp[i][1])
            curr_max = max(nums[i] , dp[i][0] , dp[i][1])
            dp[i] = [curr_min , curr_max]
            ans = max(ans , curr_max)

        return ans
        '''

        #tabulation for space otpimization
        prev_min = nums[0]
        prev_max = nums[0]
        ans = nums[0]
        for i in range(1 , n):
            temp_min = prev_min * nums[i]
            temp_max = prev_max * nums[i]
            curr_min = min(nums[i] , temp_min , temp_max)
            curr_max = max(nums[i] , temp_min , temp_max)
            
            ans = max(ans , curr_max)
            prev_min = curr_min 
            prev_max = curr_max
        return ans
            