
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        total = sum(nums)
        target = total //2
        if sum(nums) % 2 != 0:
            return False
        memo = {}
        def dfs( i , curr):
            if curr == target:
                return True
            if  i == len(nums) or curr > target:
                return False
            if (i , curr) in memo:
                return memo[(i,curr)]
            #take
            take = dfs(i+1 , nums[i] + curr)
            #skip
            skip = dfs(i+1 , curr)
            memo[(i,curr)] = skip or take
            return memo[(i , curr)]

        return dfs(0 , 0)
        
        total = sum(nums)
        target = total //2
        if sum(nums) % 2 != 0:
            return False
        n = len(nums)
        dp =[[False] * (target + 1) for i in range(n+1)]
        #sum 0 is always possible by choosing nothing 
        #dp[i][s] = can we get s by starting at i
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1,n+1):
            for s in range(1 , target+1):
                if s >= nums[i-1]:
                    dp[i][s] = dp[i-1][s] or dp[i-1][s-nums[i-1]]
                else:
                    dp[i][s] = dp[i-1][s]

        return dp[n][target]

        '''
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = {0}

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()

            for s in dp:
                nextDP.add(s)                 # don't take
                nextDP.add(s + nums[i])      # take

            dp = nextDP

        return target in dp
