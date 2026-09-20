class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        '''
        def dfs(i , j):
            if i >j:
                return 0 
            if dp[i][j] != -1:
                return dp[i][j]
            mini = float('-inf')
            for idx in range(i , j+1):
                dp[i][j] = nums[i-1] * nums[idx] * nums[j+1] + dfs(i,idx-1) + dfs(idx+1 , j)
                mini = max(mini , dp[i][j])
                dp[i][j] = mini
            return dp[i][j]

        
        return dfs(1 ,n)
    '''
        #basecase
        dp = [[0] * (n+2) for i in range(n+2)]
        for i in range(n , 0 , -1):
            for j in range(i,n+1):
                    mini = float('-inf')
                    for idx in range(i ,j+1):
                        cost  = nums[i-1] * nums[idx] * nums[j+1] + dp[i][idx-1] + dp[idx+1][j]
                        mini = max(mini , cost)
                    dp[i][j] = mini

                    
        return dp[1][n]

        
            