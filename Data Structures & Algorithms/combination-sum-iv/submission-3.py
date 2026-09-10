class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        memo = {}
        def dfs(curr):
            if curr > target:
                return 0 
            if curr == target:
                return 1
            res = 0
            if curr in memo:
                return memo[curr]
            for num in nums:
                res += dfs(curr + num)
            memo[curr] = res
            return memo[curr]

        return dfs(0)
        '''
        dp = defaultdict(int)
        dp[0] = 1
        for total in range(1 , target + 1):
            dp[total] = 0
            for n in nums:
                if n <= total:
                    dp[total] += dp[total -n]
        return dp[total]