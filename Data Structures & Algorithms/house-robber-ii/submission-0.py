class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
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
        memo={}
        skip_first = dfs(1,n-1)
        return max( skip_last , skip_first)
